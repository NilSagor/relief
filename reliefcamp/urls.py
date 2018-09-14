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
from django.conf.urls import url
from django.views.generic import TemplateView

from refegue import views


app_name = 'refegue'
urlpatterns = [	
	path('', views.HomePageView.as_view(), name = 'home'),
	path('request/', views.CreateRequest.as_view(), name = 'requestview'),
	path('req_success/', views.ReqSuccess.as_view(), name = 'req_successview'),
    path('collection_center/', views.CollectionCenterView.as_view(), name = 'collection_centers_view'),
    path('collection_centers/', TemplateView.as_view(template_name = 'refegue/collectioncenter_state_select.html'), name = 'collection_centers_district_select'),
    url(r'collection_centers/(?P<location>\w+)/$', views.CollectionCenterListView.as_view(), name = 'collection_centers_list'),
    path('volunteer/', views.RegisterVolunteer.as_view(), name = 'registerview'),
    path('volunteerdata/', views.volunteerdata, name= 'volunteerdata'),
    path('NGO/', views.RegisterNGO.as_view(), name = 'ngoregisterview'),
    

    path('admin/', admin.site.urls),
]
