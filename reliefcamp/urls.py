"""reliefcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, reverse

from django.views.generic import TemplateView

from refegue import views

urlpatterns = [
	
	path('', views.HomePageView.as_view(), name = 'home'),
	path('request/', views.CreateRequest.as_view(), name = 'requestview'),
	path('req_success/', views.ReqSuccess.as_view(), name = 'req_successview'),
    path('admin/', admin.site.urls),
]
