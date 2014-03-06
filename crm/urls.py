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
    url(r'^show/', views.show),
    #url(r'^sns/', views.sns),
    url(r'^crm/', views.crm),
    url(r'^csv/', views.to_csv),
    url(r'^doc/', views.doc),
	url(r'^image/(?P<path>.*)', views.show_image),
	url(r'^info/', views.info),
	url(r'^login/', views.login),
	url(r'^register/', views.register),
	#url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),

	#url(r'^static/admin/css/base.css$', views.load_css),
)
