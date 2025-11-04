from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("vaibhav/", views.vaibhav, name="vaibhav"),
    path("greet/<str:name>/", views.greet, name="greet"),
    path("html/", views.html, name="html"),
    
]