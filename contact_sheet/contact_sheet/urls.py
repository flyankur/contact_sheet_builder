from django.conf.urls import patterns, include, url
import settings
#from contact_sheet.views import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('contact_sheet.views',
	url(r'^$', 'home'),
    # Examples:
    # url(r'^$', 'contact_sheet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
