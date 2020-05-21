import requests
import json
import urllib2

#Using Requests
print "Using REQUESTS"
print ""

try:
	l = requests.Session().get("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&maxResults=10&key=AIzaSyAYMxpreWpRpp5j8vvSlYywdfAFMatqyZk") 
	resp_dict = json.loads(l.content)

except requests.exceptions.RequestException as e:
	raise SystemExit(e)

for i in resp_dict['items']:
     print "Video Title: ",i['snippet']['title']
     print "Video Id",i['id']
     print "Video Category",i['snippet']['categoryId']
     print "Rating",i['contentDetails']['contentRating']
     print "Embed Url is","https://www.youtube.com/watch?v=123123asdsad12"+i['id']
     print ""

print ""
#using urllib2

print "Using URL LIB2"
print ""

try:
	response = urllib2.urlopen('https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&maxResults=10&key=AIzaSyAYMxpreWpRpp5j8vvSlYywdfAFMatqyZk')
	resp_dict = json.loads(l.content)

except HTTPError:
	print 'Could not retrieve data'

for i in resp_dict['items']:
     print "Video Title: ",i['snippet']['title']
     print "Video Id",i['id']
     print "Video Category",i['snippet']['categoryId']
     print "Rating",i['contentDetails']['contentRating']
     print "Embed Url is","https://www.youtube.com/watch?v=123123asdsad12"+i['id']







