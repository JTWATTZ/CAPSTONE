from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path("<str:user>", views.hungry_name, name="hungry_name"),#15/Dec/2022 this is a greeting
    path('about/', views.about, name = 'about'),
    path('recipe/', views.recipe, name = 'recipe'),#must work on getting this page
    #to display the output
    # path('home')
]