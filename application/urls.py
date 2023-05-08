from . import views
from django.urls import path, include 
from .views import *
urlpatterns = [
    path("", views.industry_summary_list, name="filter"), 
    path("likelihood/", views.likelihood, name="likelihood"),
    path("intensity/", views.intensity, name="intensity"),
    path("relevance/", views.relevance, name="relevance"),
]

