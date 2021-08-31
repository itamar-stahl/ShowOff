from django.urls import path
from . import views

app_name = "stats_presentor"

urlpatterns = [
     path("", views.index, name="index"),
     path("fake", views.fake, name="fake"),
     path("nfake", views.fake_new, name="fake_new"),
     path("fake/<str:period>", views.fake, name="fake")
     
 ]