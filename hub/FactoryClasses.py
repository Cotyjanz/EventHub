# FactoryClasses.py
# Author: Coty Janz
from abc import ABC, abstractmethod

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

'''
Terminology used is that of the "gang of four" description of the factory design pattern
 This code can be further decoupled by fixing the render_context issue we got with 
 HttpResponse and Template.render(). To keep this functional and not waste time, we instead
 use the Render shortcut on our page.
''' 

# Abstract Creator class
class AbstractEventPosterFactory(ABC):
    @abstractmethod
    def createPage(self, eventDetails, format):
        pass

    def constructTemplatePath(self, layout):
        url = 'hub/' + layout + '.html'
        return url

# Concrete Creator class
class EventPosterFactory(AbstractEventPosterFactory):
    def createPage(self, eventDetails, format):
        layout = eventDetails['event'].poster_layout
        path = self.constructTemplatePath(layout)

        if format == 'html' :
            htmlPoster = HTMLEventPoster()
            concretePoster = htmlPoster.produceResponse(eventDetails, path)
        elif format == 'png' :
            pngPoster = PNGEventPoster()
            concretePoster = pngPoster.produceResponse(eventDetails, path)

        return concretePoster 

# Abstract Product class
class AbstractEventPoster(ABC):
    @abstractmethod
    def produceResponse(self, eventDetails, templatePath):
        pass

# Concrete Product Class - render the event poster as an html page
class HTMLEventPoster(AbstractEventPoster):
    def produceResponse(self, eventDetails, templatePath):
        # We would prefer to create httpResponse objects here without the render shortcut
        return render(eventDetails['request'], templatePath, eventDetails)

# Concrete Product Class - render the event poster as an image
# this class represents the event poster rendered as a PNG image instead of an HTML/css document
class PNGEventPoster(AbstractEventPoster):
    def produceResponse(self, eventDetails, templatePath):
        # TODO: create rendered image using third party library like imgkit
        renderedImage = None;
        return HttpResponse(renderedImage, content_type='image/png')