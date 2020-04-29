
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
    path('activities/facilities/',views.activities_facilities, name='activities_facilities'),
    path('activities/results/', views.activities_results, name='activities_results'),
    path('contact/',views.contact, name="contact"),
    path('contactmessage/',views.contactmessage, name="contactmessage"),
    path('gallery/', views.gallery, name="gallery"),
    path('gallerydetail/<int:id>',views.gallerydetail,name='gallerydetail'),

    path('events/<int:id>/',views.single_event,name="single_event"),
    path('notices/<int:id>/',views.single_notice, name="single_notice"),

    path('admin/', admin.site.urls),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
