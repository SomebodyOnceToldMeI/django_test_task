from django.urls import path
from . import views
urlpatterns = [path('post/create', views.create_post, name = 'create_post'),
               path('post/like', views.like_post, name='like_post'),
               path('post/unlike', views.unlike_post, name='unlike_post'),
               path('user/signup', views.signup_user, name='signup_user'),
               path('user/login', views.login_user, name='login_user')]