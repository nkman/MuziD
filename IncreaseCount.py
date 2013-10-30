import urllib
import urllib2
import json
import requests

print "Connecting to sdslabs.co.in/muzi\n"
muzi_url = 'http://www.sdslabs.co.in/muzi/ajax/album/list.php'
url_is = urllib2.urlopen(muzi_url).read()
print "Connected\n"
alb = raw_input("Enter album name(It is case sensitive)\n")
#alb = 'Speak Now'

print "Getting Song list"
decoded_data = json.loads(url_is)
i = 0 
name_data = decoded_data[i]['name']
while(name_data != alb):
	i = i+1
	name_data = decoded_data[i]['name']
alb_id_f = decoded_data[i]['id']
song_content_url = 'https://www.sdslabs.co.in/muzi/ajax/album/?id=%d' % int(alb_id_f)
#print song_content_url

album_url = urllib2.urlopen(song_content_url).read()
decoded_data_album = json.loads(album_url)
print decoded_data_album['tracks'][0]['id']
last = 0
vi = len(decoded_data_album['tracks'])
i = 0
while(i < vi):
	print str(i) + "  " + decoded_data_album['tracks'][i]['title']
	i = i + 1
input_num = raw_input("Choose song \n")
#input_num = 1

songmain_id = decoded_data_album['tracks'][int(input_num)]['id']
increaseCount_url = 'https://sdslabs.co.in/muzi/ajax/track/log.php?id=%d' % int(songmain_id)
count = raw_input("Increase count By\n")
#count = 10

i =0
print "Started...."
for i in range(0,int(count)):
	requests.get(increaseCount_url)
	print "%d requests sent." % int(i+1)
	i = i + 1
print "count has been increased by %d time\n" % int(count)
