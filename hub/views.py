from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from hub.forms import RegisterForm, EventDetailsForm, EventRSVPForm

from django.contrib.sessions.models import Session
from django.contrib.auth.forms import AuthenticationForm

from hub.FactoryClasses import *
from hub.models import *

# Render the index page, query the database for events to populate cards
def DIY_index(request):
 	public_events = EventDetails.objects.all().filter(Is_public=True).order_by('-event_id')[:10]
 	context = {
 		'events' : public_events
 	}
 	# render() looks for HTML templates inside templates directory inside app directory
 	return render(request, 'hub/index.html', context)

# Render the user page and populate it with events
def DIY_user_page(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
       username = request.session['username']
       user = User.objects.get(username=username)
    events = EventDetails.objects.all().filter(Is_public=True).order_by('-event_id')[:10]
    user_events = EventDetails.objects.all().filter(u_id=user.id)
    context = {
        'events' : events,
        'userevents': user_events,
        'username' : username
    }
    return render(request, 'hub/user_page.html', context)

# Handle requests for event posters, currently this is just an html formatted page
# we impliment a Factory which would allow us to generate posters in many other formats
def event_detail(request, primary_key):
    if request.method == 'POST':
        form = EventRSVPForm(request.POST)
        rsvp_event = EventDetails.objects.get(event_id = primary_key)
        if form.is_valid():
            event_rsvp = form.save(commit=False)
            rsvp_event.Is_rsvp += event_rsvp.Is_rsvp
            rsvp_event.save()
            return redirect('/')

        event = get_object_or_404(EventDetails, event_id=primary_key)
        context = {
            'requet' : request,
            'event' : event,
        }
        # Create instance of EventPosterFactory
        factory = EventPosterFactory()
        response = factory.createPage(context, "html")
        return response

    if request.method == 'GET':
        event = get_object_or_404(EventDetails, event_id=primary_key)
        rsvp_form = EventRSVPForm(request.POST)
        context = {
            'request' : request,
            'event' : event,
            'event_rsvp' : rsvp_form,
            }
        # Create instance of EventPosterFactory
        factory = EventPosterFactory()
        response = factory.createPage(context, "html")
        return response


# handle signin requests form submission and session control
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            events = EventDetails.objects.all().filter(Is_public=True).order_by('-event_id')[:10]
            user_events = EventDetails.objects.all().filter(u_id=user.id)
            context = {
                'events' : events,
                'usersevents': user_events,
                'username' : username
            }
            #return redirect('/DIY_user_page', context)
            response =  redirect('/DIY_user_page', context)
            response.set_cookie('last_connection', datetime.now())
            response.set_cookie('username', datetime.now())
            return response
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    if request.method == 'GET':
        if 'username' in request.COOKIES and 'last_connection' in request.COOKIES and not request.user.is_anonymous:
            username = request.COOKIES['username']
            last_connection = request.COOKIES['last_connection']
            last_connection_time = datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_connection_time).seconds < 100:
                return redirect('DIY_user_page')
            else:
                form = AuthenticationForm(request.POST)
                return render(request, 'registration/login.html', {'form': form})
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})

# handle logout requests
def signout(request):
    try:
        Session.objects.all().delete()
        logout(request)
        return redirect("/")
    except:
        pass
    return redirect("/")

# handle registration form validation and submission
def register(request):
	if request.method == "GET":
		return render(request, "registration/register.html",{"form": RegisterForm})
	elif request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect(reverse("DIY_index"))
		else:
			messages.error(request, 'Error Processing Your Request')
			context = {'form': form}
			return render(request, 'registration/register.html', context)

# Handle creation of new events and creating instances of EventDetails 
def DIY_create(request):
    if request.method == 'POST':
        form = EventDetailsForm(request.POST)
        if form.is_valid():
            event_details = form.save(commit=False)
            event_details.u_id = request.user
            event_details.save()
            return redirect('DIY_user_page')
        else:
            messages.error(request, form.errors)
            return render(request, 'hub/create.html')

    if request.method == 'GET':
        context = {'form': EventDetailsForm}
        return render(request, 'hub/create.html', context)