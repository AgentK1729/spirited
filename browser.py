import gtk, webkit
import datetime
from moodmap import MoodMap, MoodMatrix
from webpage_sentiment import wsent
# Previous timestamp
global prev_ts, prev_site, arous, val
prev_ts = 0
prev_site = 'http://google.com'
arous, val = 0, 0
from urllib import urlopen
from json import loads

class Browser():
	def __init__(self):
		global prev_ts, prev_site, arous, val
		prev_ts = datetime.datetime.now()
		# Create window
		self.much_window = gtk.Window()
		color = gtk.gdk.color_parse(MoodMap[MoodMatrix[arous][val]])
		self.much_window.modify_bg(gtk.STATE_NORMAL, color)
		self.much_window.connect('destroy', lambda w: gtk.main_quit())
		screen = self.much_window.get_screen()
		self.much_window.resize(screen.get_width(), screen.get_height())

		# Create navigation bar
		self.so_navigation = gtk.HBox()

		self.many_back = gtk.ToolButton(gtk.STOCK_GO_BACK)
		self.such_forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
		self.very_refresh = gtk.ToolButton(gtk.STOCK_REFRESH)
		self.wow_address_bar = gtk.Entry()

		self.many_back.connect('clicked', self.go_back)
		self.such_forward.connect('clicked', self.go_forward)
		self.very_refresh.connect('clicked', self.refresh_page)
		self.wow_address_bar.connect('activate', self.load_page)

		self.so_navigation.pack_start(self.many_back, False)
		self.so_navigation.pack_start(self.such_forward, False)
		self.so_navigation.pack_start(self.very_refresh, False)
		self.so_navigation.pack_start(self.wow_address_bar)

		# Create view for webpage
		self.very_view = gtk.ScrolledWindow()
		self.such_webview = webkit.WebView()
		#self.such_webview.open('http://google.com')
		self.such_webview.connect('title-changed', self.change_title)
		self.such_webview.connect('load-committed', self.change_url)
		self.very_view.add(self.such_webview)

		# Add everything and initialize
		self.wow_container = gtk.VBox()
		self.wow_container.pack_start(self.so_navigation, False)
		self.wow_container.pack_start(self.very_view)

		self.much_window.add(self.wow_container)
		self.much_window.show_all()
		

	def load_page(self, widget):
		global prev_ts, prev_site, arous, val
		Time = int((datetime.datetime.now()-prev_ts).total_seconds())
		response = urlopen("https://api.thingspeak.com/channels/96130/feeds.json?results=2")
		j = loads(response.read())['feeds'][-1]
		darous = float(j['field2']) - Time
		dval = float(j['field3']) - wsent(prev_site)
		urlopen("https://api.thingspeak.com/update?api_key=M4U7EH8VE65CYHD1&field1=%s&field2=%s&field3=%s" % (prev_site, Time, wsent(prev_site)))
		print darous, dval
			
		
		# change arous and val values
		if darous > 0:
			if arous == 0:
				pass
			else:
				arous -= 1
		elif darous == 0:
			pass
		else:
			if arous == 5:
				pass
			else:
				arous += 1
				
		if dval > 0:
			if val == 0:
				pass
			else:
				val -= 1
		elif val == 0:
			pass
		else:
			if val == 1:
				pass
			else:
				arous += 1
				
		print arous, val
		
		# change color
		color = gtk.gdk.color_parse(MoodMap[MoodMatrix[arous][val]])
		self.much_window.modify_bg(gtk.STATE_NORMAL, color)
		
		so_add = self.wow_address_bar.get_text()
		if so_add.startswith('http://') or so_add.startswith('https://'):
			self.such_webview.open(so_add)
		else:
			so_add = 'http://' + so_add
			self.wow_address_bar.set_text(so_add)
			self.such_webview.open(so_add)
			
		prev_site = so_add
		prev_ts = datetime.datetime.now()
		self.run()
			
		

	def change_title(self, widget, frame, title):
		self.much_window.set_title(title)

	def change_url(self, widget, frame):
		uri = frame.get_uri()
		self.wow_address_bar.set_text(uri)

	def go_back(self, widget):
		self.such_webview.go_back()

	def go_forward(self, widget):
		self.such_webview.go_forward()

	def refresh_page(self, widget):
		self.such_webview.reload()
		
	def run(self):
		gtk.main()