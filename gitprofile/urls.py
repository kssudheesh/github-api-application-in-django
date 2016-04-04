from django.conf.urls import url

from gitprofile import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
]
