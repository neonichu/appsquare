#!/usr/bin/env python

##
APP_TOKEN = 'obtain-app-token-from-ADN'
FOURSQUARE_CLIENT_ID = 'obtain-foursquare-client-id'
FOURSQUARE_CLIENT_SECRET = 'obtain-foursquare-client-secret'
FOURSQUARE_USER_TOKEN = None
USERNAME = 'your-user-name' # for testing only
##

import logging
logging.basicConfig()

import sys
sys.path.append('vendor/apppy')

def getADNClient():
    from apppy import apppy
    adn_client = apppy(access_token=APP_TOKEN)

    r = adn_client.getUser("me")
    assert r.json()['data']['username'] == USERNAME

    return adn_client

def getFoursquareClient():
    from foursquare import Foursquare
    import webbrowser

    if FOURSQUARE_USER_TOKEN:
	    foursq_client = Foursquare(access_token=FOURSQUARE_USER_TOKEN, version='20130415')
    else:
	    foursq_client = Foursquare(client_id=FOURSQUARE_CLIENT_ID, 
		    client_secret=FOURSQUARE_CLIENT_SECRET, redirect_uri='http://vu0.org/projects/appsquare/foursquare.html',
		    version='20130415')
	    webbrowser.open(foursq_client.oauth.auth_url())
	    foursq_code = raw_input('Please paste the code from the website: ')
	    access_token = foursq_client.oauth.get_token(foursq_code)
	    print 'FOURSQUARE_USER_TOKEN for the script: %s' % access_token
	    sys.exit(0)
    
    return foursq_client

def getFoursquareCheckins():
    return getFoursquareClient().users.all_checkins() #['checkins']['items']

def getOhaiChannel():
	channels = []

	for channel in getADNClient().getUserSubscribedChannel().json()['data']:
		if channel['type'] == 'net.app.ohai.journal':
			if not channel['readers']['immutable'] and channel['writers']['immutable']:
				if len(channel['writers']['user_ids']) == 0:
					channels.append(channel)

	channels.sort(key=lambda channel: channel['id'])
	return channels[0]

def getOhaiPosts():
	channel = getOhaiChannel()
	return getADNClient().getChannelMessage(channel['id'], include_annotations=1).json()['data']

if __name__ == '__main__':
	from datetime import datetime

	channel = getOhaiChannel()
	client = getADNClient()

	for checkin in getFoursquareCheckins():
		if checkin['type'] == 'venueless':
			continue

		checkin_date = datetime.fromtimestamp(checkin['createdAt']).isoformat()
		post_text = checkin.get('shout', 'Checked in with Foursquare.')
		annotations = [{ 
			'type': 'net.app.ohai.location',
			'value': {
				'country_code': checkin['venue']['location']['cc'],
				'address': checkin['venue']['location'].get('address', ''),
				'postcode': checkin['venue']['location'].get('postalCode', ''),
				'region': checkin['venue']['location'].get('state', ''),
				'locality': checkin['venue']['location'].get('city', ''),
				'id': checkin['venue']['id'],
				'name': checkin['venue']['name'],
				'latitude': checkin['venue']['location']['lat'],
				'longitude': checkin['venue']['location']['lng']
			},
		},
		{
			'type': 'net.app.ohai.displaydate',
			'value': { 'date': checkin_date + 'Z' }
		}]

		client.createMessage(channel['id'], text=post_text, annotations=annotations)
