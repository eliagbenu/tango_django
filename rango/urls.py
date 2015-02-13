from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/',views.about,name='about'),#in rango app
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),    
	url(r'^add_category/$', views.add_category, name='add_category'),	 
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),	
    url(r'^register/$', views.register, name='register'), 	 
    url(r'^login/$', views.user_login, name='login'), 	 
    url(r'^restricted/', views.restricted, name='restricted'),    
    url(r'^logout/$', views.user_logout, name='logout'),    
)
