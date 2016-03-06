from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musicplayer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
					   
	url(r'^play/', 'musicplayer.player.views.home'),
					   
	url(r'^choose-next/', 'musicplayer.player.views.choose'),
					   
	url(r'^logout/', 'musicplayer.player.views.logout'),
)
