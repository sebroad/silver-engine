from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
import re

# Create your views here.
def search(request, terms):
	results = Definition.objects.filter(name__icontains=terms)
	c = dict({'definitions': results, 'title': 'Silver Engine Learning Objects', })
	t = loader.get_template("Definitions.html")
	return HttpResponse(t.render(c))	
