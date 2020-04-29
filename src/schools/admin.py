from django.contrib import admin
from django.contrib.auth.models import Group
from .models import IndexImage, Notice, Event, Staff, BoardofDirector, Result,ContactMessage, Gallery, GalleryImage




class IndexImageAdmin(admin.ModelAdmin):
	list_display = ['index_image','active','timestamps','updated']
	list_filter = ['updated']
	search_fields = ['index_image']
	class Meta:
		model = IndexImage


class NoticeAdmin(admin.ModelAdmin):
	list_display = ['notice_title','notice_description','notice_file','updated']
	list_filter = ['updated']
	search_fields = ['notice_title','notice_description']
	class Meta:
		model = Notice


class EventAdmin(admin.ModelAdmin):
	list_display = ['event_title','event_date','event_time','event_location','updated']
	list_filter = ['updated']
	search_fields = ['event_title','event_date','event_location','event_time','event_details']
	class Meta:
		model = Event

class StaffAdmin(admin.ModelAdmin):
	list_display = ['staff_name','staff_designation','staff_telephone','staff_type','updated']
	list_filter = ['updated']
	search_fields = ['staff_name','staff_designation']
	class Meta:
		model = Staff

class BoardofDirectorAdmin(admin.ModelAdmin):
	list_display = ['director_name','director_designation','director_telephone','updated']
	list_filter = ['updated']
	search_fields = ['director_name','director_designation']
	class Meta:
		model = BoardofDirector


class ResultAdmin(admin.ModelAdmin):
	list_display = ['result_title','result_file','updated']
	list_filter = ['updated']
	search_fields = ['result_title']
	class Meta:
		model = Result


class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ['contact_name','contact_email','contact_subject','contact_message']
	list_filter = ['timestamps']
	search_fields = ['contact_name','contact_email','contact_subject']
	class Meta:
		model = ContactMessage


class GalleryImageAdmin(admin.StackedInline):
	model = GalleryImage

class GalleryAdmin(admin.ModelAdmin):
	inlines = [GalleryImageAdmin]
	list_display =['gallery_name','updated']
	class Meta:
		model = Gallery

class GalleryImageAdmin(admin.ModelAdmin):
	pass



# Register your models here.

admin.site.unregister(Group)
admin.site.register(IndexImage,IndexImageAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(BoardofDirector, BoardofDirectorAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(GalleryImage,GalleryImageAdmin)






admin.site.site_header = "SNEBS Admin"
admin.site.site_title = "SNEBS Admin Portal"
admin.site.index_title = "Welcome to Saraswati Niketan Admin Panel"

