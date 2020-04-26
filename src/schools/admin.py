from django.contrib import admin
from .models import IndexImage, Notice, Event, Teacher, BoardofDirector, Result



# Register your models here.

admin.site.register(IndexImage)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Teacher)
admin.site.register(BoardofDirector)
admin.site.register(Result)



admin.site.site_header = "SNEBS Admin"
admin.site.site_title = "SNEBS Admin Portal"
admin.site.index_title = "Welcome to Saraswati Niketan Admin Panel"

