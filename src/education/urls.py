"""education URL Configuration

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
from schools import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

	path('', views.home, name="home"),
	path('about-us/introduction',views.about_introduction,name="about_introduction"),
    path('about-us/board-of-directors',views.about_boardofdirectors,name='about_boardofdirectors'),
    path('about-us/staffs',views.about_staffs,name='about_staffs'),
	path('events/',views.event, name="event"),
	path('notices/',views.notice, name="notice"),
    path('activities/admissions/',views.activities_admissions, name='activities_admissions'),
    path('activities/results/', views.activities_results, name='activities_results'),
    path('contact/',views.contact, name="contact"),

    path('events/<int:id>/',views.single_event,name="single_event"),
    path('notices/<int:id>/',views.single_notice, name="single_notice"),

    path('admin/', admin.site.urls),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
