from django.conf.urls import patterns, url
from portal import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
)
