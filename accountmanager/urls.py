"""accountmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('admin/', admin.site.urls),
    path('income/',include('income.urls')),
    path('expenses/',include('expenses.urls')),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views._login,name='login'),
    path('logout/',views._logout,name='logout')
]