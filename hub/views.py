from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader

from hub.models import *

# note: request object is an HttpRequestObject, it has information about
#  request, such as the method, which can take several values including GET and POST
def DIY_index(request):
 	#public_events = EventDetails.objects.all()
 	# This query cannot be tested until the django admin is setup
 	public_events = EventDetails.objects.all().filter(Is_public=True).order_by('-event_id')[:10]
 	context = {
 		'events' : public_events
 	}
 	# render() looks for HTML templates inside templates directory inside app directory
 	return render(request, 'hub/index.html', context)

# This is the view which handles urls for the event pages themselves
def event_detail(request, primary_key):
 	# get_object_or_404 shortcut will display a 404 page if the object DNE
 	event = get_object_or_404(EventDetails, event_id=primary_key)
 	context = {
 		'event' : event
 	}
 	# event_page.html is the parent to all the potential templates which might
 	#   be choosen by the user
 	return render(request, 'hub/event_page.html', context)

def DIY_signup(request):
    template = loader.get_template('hub/signup.html')
    return HttpResponse(template.render())

def DIY_user_page(request):
    template = loader.get_template('hub/user_page.html')
    return HttpResponse(template.render())

def DIY_create(request):
    template = loader.get_template('hub/create.html')
    return HttpResponse(template.render())