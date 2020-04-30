from django.shortcuts import render, redirect, get_object_or_404
from .models import IndexImage, Notice, Event, Staff, BoardofDirector, Result, Gallery, GalleryImage
from django.db.models import Q
from django.http import HttpResponse, FileResponse, Http404
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .forms import ContactMessageForm
from django.contrib import messages
import os
# Create your views here.

def home(request):

	images = IndexImage.objects.filter(active=1).order_by('-id')[:4]
	notices = Notice.objects.filter().order_by('-id')[:10]
	events = Event.objects.filter().order_by('-id')[:4]
	template = 'schools/index.html'
	context = {'all_images': images, 'all_notices':notices,'all_events':events}
	return render(request, template, context)
	



#About Views

def about_introduction(request):
	try:
		images = IndexImage.objects.filter(active=1).order_by('-id')[:1]
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
		teaching_staffs = Staff.objects.filter(staff_type="teaching")
		non_teaching_staffs = Staff.objects.filter(staff_type="non_teaching")
		template = 'schools/about_staffs.html'
		context = {'teaching_staffs':teaching_staffs, 'non_teaching_staffs':non_teaching_staffs}
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


def activities_facilities(request):
	try:
		template = 'schools/activities_facilities.html'
		context = {}
		return render(request,template,context)
	except:
		raise Http404("Page Not Found")



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



def gallery(request):
	template = 'schools/gallery.html'
	gallery = Gallery.objects.all().order_by('-id')
	context = {'my_gallery':gallery}
	return render(request, template, context)


def gallerydetail(request,id):
	gallery = get_object_or_404(Gallery,id=id)
	images = GalleryImage.objects.filter(gallery=gallery)
	template = 'schools/gallerydetail.html'
	context = {'my_gallery':gallery,'my_images':images}
	return render(request,template,context)



def search(request):
	template = 'schools/search.html'
	if request.method == "GET":
		query = request.GET['query']	
		print(query)
		if query:
			match_notices = Notice.objects.filter(Q(Notice._meta.object_name__icontains=query) | Q(notice_title__icontains=query)|
										 Q(notice_description__icontains=query)
										 )
			match_events = Event.objects.filter(Q(event_title__icontains=query) |
												Q(event_details__icontains=query)|
												Q(event_location__icontains = query)
												)
			match_staffs = Staff.objects.filter(Q(staff_name__icontains = query) |
												Q(staff_designation__icontains=query) 
												)
			match_directors = BoardofDirector.objects.filter(Q(director_name__icontains= query) |
															 Q(director_designation__icontains=query) 
															 )
			match_results = Result.objects.filter(Q(result_title__icontains=query) 
													)
			match_gallery = Gallery.objects.filter(Q(gallery_name__icontains=query) 
														)
			if match_notices or match_events or match_staffs or match_directors or match_results or match_gallery:
				context = {'match_notices':match_notices,'match_events':match_events,'match_staffs':match_staffs,
				'match_directors':match_directors,'match_results':match_results,'match_gallery':match_gallery}
				return render(request,template,context)
			else:
				messages.error(request,'No search results found')
		else:
			return HttpResponseRedirect('search/')
	
	return render(request, template)


def contact(request):
	try:
		template = 'schools/contact.html'
		form = ContactMessageForm()
		context = {'form':form}
		return render(request, template, context)
	except:
		raise Http404("Post not found")


def contactmessage(request):
	try:
		if request.method == "POST":
			form = ContactMessageForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/contact/')
			form = ContactMessageForm()
		else:
			return redirect('/contact/')
	except:
		raise Http404("Page Not Found")

	# form = ContactMessageForm()
	# return render(request, template, {})




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

