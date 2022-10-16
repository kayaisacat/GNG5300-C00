# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
from .models import GeeksModel
from .forms import GeeksForm
from django.forms import modelformset_factory
# importing formset_factory
from django.forms import formset_factory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


# get datetime
import datetime


# create a function
def geeks_view(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
    
	# return response
	return HttpResponse(html)

# creating a home view
def home_view(request):
	context ={}

	# create object of form
	form = GeeksForm(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "home.html", context)


def formset_view(request):
    context ={}
  
    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = formset_factory(GeeksForm, extra = 3)
    formset = GeeksFormSet(request.POST or None)
      
    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

  
def modelformset_view(request):
    context ={}
  
    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = modelformset_factory(GeeksModel, fields =['title', 'description'], extra = 3)
    formset = GeeksFormSet()
  
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)


class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)


# pass id attribute from urls
# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)

from django.http import HttpResponse
from django.views import View

class MyView(View):
	def get(self, request):
		# <view logic>
		return HttpResponse('result')


class GeeksCreate(CreateView):
 
    # specify the model for create view
    model = GeeksModel
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']


# import generic UpdateView
from django.views.generic.edit import UpdateView

# Relative import of GeeksModel
from .models import GeeksModel

class GeeksUpdateView(UpdateView):
	# specify the model you want to use
	model = GeeksModel

	# specify the fields
	fields = [
		"title",
		"description"
	]

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/"


# # The one way from httpresonse
# def home(request):
#     return HttpResponse('Home page')

# def room(request):
#     return HttpResponse('Room')

# # The second way from reader using setting.py in templates
# def home(request):
#     return render(request, 'geeks/home.html')

# def room(request):
#     return render(request, 'geeks/room.html')
