from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
	# Request the context of the request
	# The context contains info such as client's machine details, for example
	context = RequestContext(request)

	# Construct a dict to pass to the template engine as its content
	# Note the key boldmessage is the same as {{ boldmessage }} in the template
	context_dict = {'boldmessage': "I am bold font from the context"}

	# Return a rendered response to send to the client
	# The first param is the template to use
	return render_to_response('rango/index.html', context_dict, context)


def about(request):
	# return HttpResponse('Rango says: Here is the about page. <a href="/rango/">Home</a>')
	context = RequestContext(request)
	return render_to_response('rango/about.html', context)