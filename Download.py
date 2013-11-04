import os
import errno
import urllib
import urllib2
import json
#import re

def Maked(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

print "Select a choice"
print "1. Download all songs from an album \n2. Select and Download a song from an album"
first_input = raw_input()  #Check the Input

muzi_url = 'http://www.sdslabs.co.in/muzi/ajax/album/list.php'
url_is = urllib2.urlopen(muzi_url).read()
alb = raw_input("Enter album name(It is case sensitive)\n")
#encounter = url_is.find(alb)
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
#print decoded_data_album['tracks'][0]['id']
last = 0
vi = len(decoded_data_album['tracks'])
i = 0
if(int(first_input) == 2):
	while(i < vi):
		print str(i) + "  " + decoded_data_album['tracks'][i]['title']
		i = i + 1
	input_num = raw_input("Choose song \n")
	name_song = decoded_data_album['tracks'][int(input_num)]['title']
	songmain_id = decoded_data_album['tracks'][int(input_num)]['id']
	songmain_url = 'http://www.sdslabs.co.in/muzi/ajax/track?id=' + str(songmain_id)
	got = urllib2.urlopen(songmain_url).read()
	dcode_got = json.loads(got)
	last_song = dcode_got['file']
	song_url = 'http://music.sdslabs.co.in/' + last_song
	namew = str(decoded_data_album['tracks'][int(input_num)]['title']) + '.mp3'
	#directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), name_song)
	#filename = os.path.join(directory, namew)
	#Maked(directory)
	#if not os.path.exists(filename):
	#	urllib.urlretrieve(song_url, filename)
	urllib.urlretrieve(song_url,namew)
	print "Song %r.mp3 has been downloaded" % str(decoded_data_album['tracks'][int(input_num)]['title'])
	#i = i + 1

elif(int(first_input) == 1):
	#print "songs are"
	while(i < vi):
		#print str(i) + "  " + decoded_data_album['tracks'][i]['title']
		
		songmain_id = decoded_data_album['tracks'][int(i)]['id']
		songmain_url = 'http://www.sdslabs.co.in/muzi/ajax/track?id=' + str(songmain_id)
		got = urllib2.urlopen(songmain_url).read()
		dcode_got = json.loads(got)
		last_song = dcode_got['file']
		song_url = 'http://music.sdslabs.co.in/' + last_song
		namew = str(decoded_data_album['tracks'][int(i)]['title']) + '.mp3'

		directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), alb)
		filename = os.path.join(directory, namew)
		Maked(directory)
		if not os.path.exists(filename):
			urllib.urlretrieve(song_url, filename)


		#urllib.urlretrieve(song_url,namew)
		print "Song %r.mp3 has been downloaded" % str(decoded_data_album['tracks'][int(i)]['title'])
		i = i + 1

