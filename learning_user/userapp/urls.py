from django.urls import path, re_path, include
from . import views

app_name = 'userapp'

urlpatterns = [
    re_path(r'^registration/',views.register,name='register'),
    re_path(r'^login/',views.user_login,name='login'),
]
