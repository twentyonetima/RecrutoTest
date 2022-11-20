from django.urls import path

from main import views

urlpatterns = [
    path('url_name/', views.get_some),
]