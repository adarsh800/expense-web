"""expenseweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import  Sign_out_View,VerificationView, Sign_in_View, Sign_up_View, forgot_password_View, new_password_View, Validate_Username_View, Validate_Email_View
urlpatterns = [
    path('sign-in/', Sign_in_View.as_view(), name = 'sign-in'),
    path('sign-out/', Sign_out_View.as_view(), name = 'sign-out'),
    path('sign-up/', Sign_up_View.as_view(), name = 'sign-up'),
    path('forgot-password/', forgot_password_View.as_view(), name = 'forgot-password'),
    path('new-password/', new_password_View.as_view(), name = 'new-password'),
    path('sign-up/validate-username/', csrf_exempt(Validate_Username_View.as_view()), name = 'validate-username'),
    path('sign-up/validate-email/', csrf_exempt(Validate_Email_View.as_view()), name = 'validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name = 'activate'),
    
]
