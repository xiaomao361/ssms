"""ssms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import imp
from django.conf.urls import url
from job import views 


urlpatterns = [

    url(r'^cmd/', views.cmd),
    url(r'^exec_cmd/', views.exec_cmd),
    url(r'^script/', views.script),
    url(r'^tasks/', views.tasks),
    url(r'^exec_script/', views.exec_script),
    url(r'^load/', views.load),
    url(r'^cancel/', views.cancel),

]
