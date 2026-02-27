from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # voice-update endpoint removed; recognition now handled in browser
]
