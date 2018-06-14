#!/usr/bin/python

import httplib2
import urllib

h = httplib2.Http(".cache")
#url = 'https://accounts.google.com/o/oauth2/token'
url = 'https://www.googleapis.com/oauth2/v4/token'
body = 
{ 
  'client_secret': 'xxx',
  'grant_type': 'refresh_token',
  'refresh_token': 'xxx',
  'client_id': 'xxx'
}
headers = {'Content-type': 'application/x-www-form-urlencoded', 'cache-control': 'no-cache'}
response, content = h.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

print(content)
