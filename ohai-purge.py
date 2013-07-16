#!/usr/bin/env python

## Delete all posts imported with appsquare

import appsquare

client = appsquare.getADNClient()

for post in appsquare.getOhaiPosts():
    if not post['source']['client_id'] == 'ZQnmKKhq8n4y2Ngej95rEg6wve67UHyk':
        continue
    client.destroyMessage(post['channel_id'], post['id'])
