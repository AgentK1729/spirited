# stack overflow
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
from successive import Word, getSentiment

def wsent(link):
	def visible(element):
		if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		    return False
		elif re.match('<!--.*-->', str(element)):
		    return False
		return True

	html = urlopen(link).read()
	soup = BeautifulSoup(html)
	texts = soup.findAll(text=True)

	visible_texts = filter(visible, texts)
	words = [Word(i, []) for i in visible_texts if i != ' ']
	return getSentiment(words)

