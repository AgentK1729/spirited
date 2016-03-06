from scipy.io.wavfile import read
from numpy import linspace
from sqlite3 import connect

def Song(object):
	def __init__(self, name, amplitude, duration):
		self.name = name
		self.amplitude = amplitude
		self.duration = duration
		
	def __lt__(self, other):
		return __cmp__(self.amplitude/self.duration, other.amplitude/other.duration)

def analyze_song(song):
	rate,data=read('/home/tejas/Files/spirited/musicplayer/musicplayer/static/%s' % song)
	y=data[:,1]
	timp=len(y)/44100.
	t=linspace(0,timp,len(y))
	return (float(max(y)), float(t[-1]))

files = ['American.mp3.wav', '03_-_goodnight_and_goodbye_-_jonas_brothers.mp3.wav', 'Greenday vs Oasis.mp3.wav', '08_-_games_-_jonas_brothers.mp3.wav', 'Green Day  - Boulevard Of Broken Dreams.mp3.wav', "We're All In This Together.mp3.wav", 'GreenDay_Wake me Up.mp3.wav', 'Play my music.mp3.wav', '02 Girl of My Dreams.mp3.wav', '06_-_still_in_love_with_you_-_jonas_brothers.mp3.wav', 'American Dragon Jake Long.mp3.wav', '13_-_year_3000_-_jonas_brothers.mp3.wav', 'Stick To The Status Quo.mp3.wav', '12_-_hollywood_-_jonas_brothers.mp3.wav', '05_-_hello_beautiful_-_jonas_brothers.mp3.wav', '10_-_inseperable_-_jonas_brothers.mp3.wav', '09_-_when_you_look_me_in_the_eyes_-_jonas_brothers.mp3.wav', 'Hold on.mp3.wav', '14_-_kids_of_the_future_-_jonas_brothers.mp3.wav', 'Start Of Something New.mp3.wav', "04_-_that's_just_the_way_we_roll_-_jonas_brothers.mp3.wav", '15_-_bbp_theme_song_(bonus_track)_-_jonas_brothers.mp3.wav', "Burnin' up.mp3.wav", '11_-_just_friends_-_jonas_brothers.mp3.wav', 'Breaking Free(Soaring, flying).mp3.wav', '07_-_australia_-_jonas_brothers.mp3.wav', 'SOS.mp3.wav']

conn = connect("songs.sqlite")
cur = conn.cursor()

for i in files:
	readings = analyze_song(i)
	cur.execute("insert into song values (?,?,?)", (i, readings[0], readings[1]))
	conn.commit()
	
conn.close()