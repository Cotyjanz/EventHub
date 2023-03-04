from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader


from hub.models import *

# note: request object is an HttpRequestObject, it has information about
#  request, such as the method, which can take several values including GET and POST
# def index(request):
# 	planned_events = PlannedEvent.objects.all()
# 	context = {
# 		'events' : planned_events
# 	}
# 	# render() looks for HTML templates inside templates directory inside app directory
# 	return render(request, 'hub/index.html', context)


# This is the view which handles urls for the event pages themselves
# def event_detail(request, primary_key):
# 	# get_object_or_404 shortcut will display a 404 page if the object DNE
# 	event = get_object_or_404(PlannedEvent, pk=primary_key)
# 	context = {
# 		'event' : event
# 	}

# 	return render(request, 'event_page.html', context)



# Create your views here.
def DIY_index(request):
     template = loader.get_template('hub/index.html')
     return HttpResponse(template.render())

def DIY_signup(request):
    template = loader.get_template('hub/signup.html')
    return HttpResponse(template.render())

def DIY_user_page(request):
    template = loader.get_template('hub/user_page.html')
    return HttpResponse(template.render())

def DIY_create(request):
    template = loader.get_template('hub/create.html')
    return HttpResponse(template.render())
     
