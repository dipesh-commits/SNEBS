from django.db import models

# Create your models here.

class IndexImage(models.Model):
	index_image = models.ImageField(null=True)
	active = models.BooleanField()
	timestamps = models.DateTimeField(auto_now_add= True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return str(self.index_image)


class Notice(models.Model):
	notice_title = models.CharField(max_length=120,null=False)
	notice_description = models.TextField(null=False)
	notice_image = models.ImageField()
	notice_file = models.FileField(null=True)
	timestamps = models.DateTimeField(auto_now_add=True,auto_now = False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __str__(self):
		return self.notice_title

	def datepublished(self):
		return self.updated.strftime('%B %d %Y')


class Event(models.Model):
	event_title = models.CharField(max_length=120,null=False)
	event_details = models.TextField(null=False)
	event_date = models.DateField(null=False)
	event_time = models.CharField(max_length=90,null=False)
	event_location = models.CharField(max_length=120,null=False)
	event_thumbnail = models.ImageField()
	timestamps = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.event_title

	def datepublished(self):
		return self.updated.strftime('%B %d, %Y')


class Teacher(models.Model):
	teacher_name = models.CharField(max_length=120, null=True)
	teacher_designation = models.CharField(max_length=120, null=True)
	teacher_image = models.ImageField(null=True)
	timestamps = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.teacher_name


class BoardofDirector(models.Model):
	director_name = models.CharField(max_length=120, null=True)
	director_designation = models.CharField(max_length=120, null=True)
	director_image = models.ImageField(null=True)
	timestamps = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.director_name


class Result(models.Model):
	result_title = models.CharField(max_length=120,null=True)
	result_file = models.FileField(null=True)
	timestamps = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.result_title

	def datepublished(self):
		return self.updated.strftime('%B %d, %Y')

	

	




