import urllib
import urllib2
import json

muzi_url = 'http://www.sdslabs.co.in/muzi/ajax/album/list.php'
url_is = urllib2.urlopen(muzi_url).read()
alb = raw_input("Enter album name(It is case sensitive)\n")

decoded_data = json.loads(url_is)
i = 0 
name_data = decoded_data[i]['name']
while(name_data != alb):
	i = i+1
	name_data = decoded_data[i]['name']
alb_id_f = decoded_data[i]['id']
song_content_url = 'https://www.sdslabs.co.in/muzi/ajax/album/?id=%d' % int(alb_id_f)
print song_content_url
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
songmain_id = decoded_data_album['tracks'][int(input_num)]['id']
songmain_url = 'http://www.sdslabs.co.in/muzi/ajax/track?id=%d' % int(songmain_id)
got = urllib2.urlopen(songmain_url).read()
dcode_got = json.loads(got)
last_song = dcode_got['file']
song_url = 'http://music.sdslabs.co.in/' + last_song
urllib.urlretrieve(song_url,'%r.mp3' %str(decoded_data_album['tracks'][int(input_num)]['title']))
print "Song %r.mp3 has been downloaded" % str(decoded_data_album['tracks'][int(input_num)]['title'])
