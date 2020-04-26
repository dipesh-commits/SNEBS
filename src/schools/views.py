from django.shortcuts import render
from .models import IndexImage, Notice, Event, Teacher, BoardofDirector, Result
from django.http import HttpResponse, FileResponse, Http404
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
# Create your views here.

def home(request):

	images = IndexImage.objects.filter(active=1).order_by('-id')[:4]
	notices = Notice.objects.filter().order_by('-id')[:10]
	events = Event.objects.filter().order_by('-id')[:2]
	template = 'schools/index.html'
	context = {'all_images': images, 'all_notices':notices,'all_events':events}
	return render(request, template, context)
	



#About Views

def about_introduction(request):
	try:
		images = IndexImage.objects.filter(active=1)[:1]
		template = 'schools/about_introduction.html'
		context = {'all_images':images}
		return render(request,template,context)
	except:
		raise Http404("Page Not Found")


def about_boardofdirectors(request):
	try:
		directors = BoardofDirector.objects.all()
		template = 'schools/about_boardofdirectors.html'
		context = {'all_directors':directors}
		return render(request, template, context)
	except:
		raise Http404("Page Not Found")



def about_staffs(request):
	try:
		staffs = Teacher.objects.all()
		template = 'schools/about_staffs.html'
		context = {'all_staffs':staffs}
		return render(request, template, context)
	except:
		raise Http404("Page Not Found")




#Event Vies
def event(request):
	try:
		events = Event.objects.all().order_by('-id')
		page = request.GET.get('page', 1)
		paginator = Paginator(events,2)
		template = 'schools/event.html'
		try:
			data = paginator.page(page)
		except PageNotAnInteger:
			data = paginator.page(1)
		except EmptyPage:
			data = paginator.page(paginator.num_pages)
		
		return render(request,template,{'all_events':data})
	except:
		raise Http404("Page Not Found")


def notice(request):
	try:
		notices = Notice.objects.all().order_by('-id')
		page = request.GET.get('page',1)
		paginator = Paginator(notices,3)
		template = 'schools/notice.html'
		try:
			data = paginator.page(page)
		except PageNotAnInteger:
			data = paginator.page(1)
		except EmptyPage:
			data = paginator.page(paginator.num_pages)

		return render(request, template, {'all_notices':data})
	except Notice.DoesNotExist:
		raise Http404("Post not found")




def activities_admissions(request):
	try:
		template = 'schools/activities_admissions.html'
		context = {}
		return render(request, template, context)
	except:
		raise Http404("Page not Found")



def activities_results(request):
	try:
		results = Result.objects.all().order_by('-id')
		page = request.GET.get('page',1)
		paginator = Paginator(results,3)
		template = 'schools/activities_results.html'
		try:
			data = paginator.page(page)
		except PageNotAnInteger:
			data = paginator.page(1)
		except EmptyPage:
			data = paginator.page(paginator.num_pages)

		return render(request, template, {'all_results':data})

	except Result.DoesNotExist:
		raise Http404("Post not found")




def contact(request):
	try:
		template = 'schools/contact.html'
		context = {}
		return render(request, template, context)
	except:
		raise Http404("Post not found")



def single_event(request,id):
	try:
		event = Event.objects.get(id=id)
		all_events = Event.objects.filter().exclude(id=id).order_by('-id')[:3]
		template = 'schools/single-event.html'
		context = {'single_event':event,'all_events':all_events}
		return render(request,template,context)
	except:
		raise Http404("Page Not Found")


def single_notice(request,id):

	try:
		document_file = Notice.objects.get(id=id)
		print(document_file.notice_file)
		filename = document_file.notice_file

		filepath = settings.MEDIA_ROOT+'/'+ str(filename)
		print(settings.MEDIA_ROOT)
		print(filepath)
		return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
	except FileNotFoundError:
		return HttpResponse(" Page Not found")

