from django.conf.urls import url, include
from django.contrib import admin
from task import views

urlpatterns = [
    url(r'^$', views.home, name = 'home' ),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # url(r'^oauth/', include('social_django.urls', namespace='social'))
]