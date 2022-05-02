from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # https://도메인
    path('result', views.result, name="result"),  # https://도메인/result
]
