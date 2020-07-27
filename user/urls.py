from .import views
from django.contrib import admin
from django.urls import path
from .views import Profile_Page, myprofile, matric_edit_view
from django.urls.conf import path

from user import views
import user.urls


app_name = 'user'

urlpatterns = [


          path('', views.myprofile, name='profile'),

          path('edit/', views.matric_edit_view, name='edit_matric'),
          path('signup', views.UserRegistration, name='signup'),

          path('login', views.user_login, name='login'),
          path('logout', views.logout_view, name='logout'),


]






