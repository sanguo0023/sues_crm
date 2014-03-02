from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
		url(r'^image/(?P<path>.*)', views.show_image),
)
