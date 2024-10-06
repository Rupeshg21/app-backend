from django.urls import path
from . import views

urlpatterns = [
    path('api/news/', views.get_news),
]
