from django.conf.urls import patterns, url
from MovieLib import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='movie_index'),
    url(r'^create$', views.CreateView.as_view(), name='movie_create'), #new line
    url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='movie_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movie_delete'),
    
)