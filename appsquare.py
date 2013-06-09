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


from apppy import *

adn_client = apppy(access_token=APP_TOKEN)

r = adn_client.getUser("me")
assert r.json()['data']['username'] == USERNAME


from foursquare import Foursquare
import webbrowser

if FOURSQUARE_USER_TOKEN:
	foursq_client = Foursquare(access_token=FOURSQUARE_USER_TOKEN)
else:
	foursq_client = Foursquare(client_id=FOURSQUARE_CLIENT_ID, 
		client_secret=FOURSQUARE_CLIENT_ID, redirect_uri='http://vu0.org/projects/appsquare/foursquare.html')
	webbrowser.open(foursq_client.oauth.auth_url())
	foursq_code = raw_input('Please paste the code from the website: ')
	access_token = foursq_client.oauth.get_token(foursq_code)
	print 'FOURSQUARE_USER_TOKEN for the script: %s' % access_token
	sys.exit(0)

print foursq_client.users.checkins()
