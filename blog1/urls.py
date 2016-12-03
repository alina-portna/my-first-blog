from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^motivation/(?P<id>[0-9]+)/$', views.motivational, name='motivational'),
	url(r'^motivation/$', views.motivation, name='motivation'),
	url(r'^music/(?P<id>[0-9]+)/$', views.music, name='music'),
]