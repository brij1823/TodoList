"""mysite URL Configuration

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
from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path("" , views.homepage , name = 'homepage'),
    path("homepage/" , views.homepage , name = 'homepage'),
    path("register" , views.register , name = "register"),
    path('logout' , views.logout_request , name = "logout"),
    path("login/" , views.login_request  , name = "login"),
    path("email/" , views.email  , name = "email"),
    path("email_compose/" , views.mail_request  , name = "email_compose"),
    path("todo/" , views.todo  , name = "todo"),
    path("delete:<int:list_id>" , views.delete  , name = "delete"),
    path("cross_off:<int:list_id>" , views.cross_off  , name = "cross_off"),
    path("uncross:<int:list_id>" , views.uncross  , name = "uncross"),
    path("edit:<int:list_id>" , views.edit  , name = "edit"),
    path("priority:<int:list_id>" , views.priority  , name = "priority"),
    path("high:<int:list_id>" , views.high  , name = "high"),
    path("medium:<int:list_id>" , views.medium  , name = "medium"),
    path("low:<int:list_id>" , views.low  , name = "low"),
    path("incomplete:<int:list_id>" , views.incomplete  , name = "incomplete"),




]
