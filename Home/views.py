from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'Jacob'

def Index(request):
    return render_to_response("home/index.html", None , context_instance=RequestContext(request))