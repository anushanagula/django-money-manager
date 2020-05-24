"""money_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from wallet import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home'),
    path('addincome/', views.addincome, name='addincome'),
    path('addexpense/', views.addexpense, name='addexpense'),
    path('mywallet/', views.mywallet, name='mywallet'),
    path('transactions/', views.transaction, name='transactions'),
    path('viewexpense/<int:expense_pk>', views.viewexpense, name='viewexpense'),
    path('viewincome/<int:income_pk>', views.viewincome, name='viewincome'),
    path('viewincome/<int:income_pk>/delete', views.deleteincome, name='deleteincome'),
    path('viewexpense/<int:expense_pk>/delete', views.deleteexpense, name='deleteexpense'),
]
