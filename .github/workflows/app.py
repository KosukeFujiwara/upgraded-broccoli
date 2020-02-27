#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import feedparser

slack = 'https://hooks.slack.com/services/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'
URL = 'http://feeds.feedburner.com/hatena/b/hotentry'

def bookmarks(event, context):
    num = 0
    for entry in feedparser.parse(URL).entries:
         print(entry.title)
         print(entry.link)
         requests.post(slack, json.dumps({"text":entry.title})
         num += 1
         if num >= 20:
             break

# call lambda_handler
if __name__ == "__main__":
    bookmarks({}, {})
