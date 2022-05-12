from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/cities/', views.CityListCreate.as_view()),
]