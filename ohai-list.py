#!/usr/bin/env python

## Print all posts from your Ohai journal to stdout

#from pprint import pprint
import appsquare

for post in appsquare.getOhaiPosts():
    #pprint(post)

    annotations = post['annotations']
    location = annotations[0]['value']['name'] if len(annotations) > 0 else 'unknown'
    print '"%s" at %s'.encode('utf-8') % (post.get('text', '').encode('utf-8'),
            location.encode('utf-8'))
