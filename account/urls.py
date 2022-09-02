from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import (
    UserLoginForm,
     PwdChangeForm, 
     PwdResetConfirmForm
     )
from . import views

app_name = 'account'

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html",
                                                authentication_form=UserLoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]