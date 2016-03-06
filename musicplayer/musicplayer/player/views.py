from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from json import loads
from urllib import urlopen
from faces import FindMood

global songs
songs = [u'Stick To The Status Quo.mp3.wav', u'Breaking Free(Soaring, flying).mp3.wav', u'Start Of Something New.mp3.wav', u'GreenDay_Wake me Up.mp3.wav', u'Greenday vs Oasis.mp3.wav', u'09_-_when_you_look_me_in_the_eyes_-_jonas_brothers.mp3.wav', u'Green Day  - Boulevard Of Broken Dreams.mp3.wav', u"We're All In This Together.mp3.wav", u'American Dragon Jake Long.mp3.wav', u'07_-_australia_-_jonas_brothers.mp3.wav', u'SOS.mp3.wav', u'13_-_year_3000_-_jonas_brothers.mp3.wav', u'08_-_games_-_jonas_brothers.mp3.wav', u'14_-_kids_of_the_future_-_jonas_brothers.mp3.wav', u'02 Girl of My Dreams.mp3.wav', u'06_-_still_in_love_with_you_-_jonas_brothers.mp3.wav', u'11_-_just_friends_-_jonas_brothers.mp3.wav', u"Burnin' up.mp3.wav", u'American.mp3.wav', u"04_-_that's_just_the_way_we_roll_-_jonas_brothers.mp3.wav", u'10_-_inseperable_-_jonas_brothers.mp3.wav', u'12_-_hollywood_-_jonas_brothers.mp3.wav', u'Hold on.mp3.wav', u'03_-_goodnight_and_goodbye_-_jonas_brothers.mp3.wav', u'05_-_hello_beautiful_-_jonas_brothers.mp3.wav', u'Play my music.mp3.wav', u'15_-_bbp_theme_song_(bonus_track)_-_jonas_brothers.mp3.wav']

def home(request):
	global songs
	try:
		return render(request, "player.html", {'song':songs[request.session['song']], 'STATIC_URL':settings.STATIC_URL, 'delay':request.session['delay']})
	except:
		request.session['song'] = 13
		return render(request, "player.html", {'song':songs[request.session['song']], 'STATIC_URL':settings.STATIC_URL, 'delay':'10'})

def choose(request):
	global songs
	response = urlopen('https://api.thingspeak.com/channels/96130/feeds.json?results=2')
	j = loads(response.read())
	request.session['delay'] = abs(float(j['feeds'][0]['field2'])-float(j['feeds'][1]['field2']))
	mood = FindMood()
	if float(j['feeds'][0]['field3'])-float(j['feeds'][1]['field3']) < 0:
		if request.session['song'] < len(songs)-1:
			request.session['song'] += 1
		else:
			pass
		if mood == -1 and request.session['song'] < len(songs)-1:
			request.session['song'] += 1
		else:
			pass
		
	else:
		if request.session['song'] > 0:
			request.session['song'] -= 1
		else:
			pass
		if mood == 1 and request.session['song'] > 0:
			request.session['song'] -= 1
		else:
			pass
	return HttpResponseRedirect("/play/")

def logout(request):
	try:
		del request.session['delay']
	except:
		pass

	try:
		del request.session['song']
	except:
		pass
	return HttpResponse("Logged out")