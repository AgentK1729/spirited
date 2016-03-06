from browser import *
from html2text import html2text
from moodmap import MoodMap
from time import sleep
from random import randint
from webpage_sentiment import wsent

sites = ["http://buzzfeed.com", "http://usanetwork.com", "http://google.com", "http://spotify.com", "http://amazon.com"]

# Initialize with HackUMBC site
b = Browser()
b.wow_address_bar.set_text("google.com")
b.load_page()
t = randint(10,30)
print "Sleeping for %d" % t
sleep(t)

# Simulate human behavior
while True:
	print "Loop entered"
	b.wow_address_bar.set_text(sites[randint(0,len(sites)-1)])
	b.load_page()
	sleep(randint(10,30))