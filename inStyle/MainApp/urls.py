# MainApp/urls.py
from django.conf.urls import url
from MainApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
