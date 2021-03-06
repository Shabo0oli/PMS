from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^report/?$', views.report, name='report'),
    url(r'^statistics/?$', views.statistics, name='statistics'),
    url(r'^sms/?$', views.sms, name='sms'),
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
]

