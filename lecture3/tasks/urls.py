from django.urls import path
from . import views

# For reference tasks app for url routes (Hyperlinks)
app_name = 'tasks'

urlpatterns = [
    path('',views.index,name="index"),
    path('add/', views.add, name = 'add'),
    
]