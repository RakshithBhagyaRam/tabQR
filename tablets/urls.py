from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablets),
    path('cough/', views.cough),
    path('cough/xyz/', views.xyz),

]
