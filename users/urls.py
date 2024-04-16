from django.urls import path
from .import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.userRegistrationView, name='register'),
    path('login/', views.CustomLoginView, name='login'),
    path('logout/', views.CustomLogoutView, name='logout'),
    path('profile/<username>', views.CustomProfileView, name='profile')
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]