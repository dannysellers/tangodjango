# from django.http import HttpResponse
from models import Category
from models import Page
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms


def index(request):
	# Obtain the context of the request
	# The context contains info such as client's machine details, for example
	context = RequestContext(request)

	# Query the database for a list of all categories currently stored
	# Order the categories by number of likes descending
	# Retrieve the top 5, or all if < 5
	# Place list in our context_dict to pass to template

	# category_list = Category.objects.order_by('-likes')[:5]

	category_list = Category.objects.order_by('name')[:5]
	context_dict = {'categories': category_list}

	# Replace spaces with underscores to retrieve URL
	for category in category_list:
		category.url = category.name.replace(' ', '_')

	# Return a rendered response to send to the client
	# The first param is the template to use
	return render_to_response('rango/index.html', context_dict, context)


def about(request):
	# return HttpResponse('Rango says: Here is the about page. <a href="/rango/">Home</a>')
	context = RequestContext(request)
	return render_to_response('rango/about.html', context)


def category(request, category_name_url):
	context = RequestContext(request)

	# Change underscores in the category name to spaces
	# The URL will have an underscore, which replaced with a space corresponds to the category
	category_name = category_name_url.replace('_', ' ')

	context_dict = {'category_name': category_name}

	try:
		# Can we find a category with the new given name?
		# If not, the .get() method raises DoesNotExist exception
		category = Category.objects.get(name=category_name)

		# Retrieve all associated pages
		# .filter method returns >= 1 model instance
		pages = Page.objects.filter(category=category)

		# Add results list to template context
		context_dict['pages'] = pages

		# We also add the category object from the database to the context directory
		# We'll use this in the template to verify that the category exists
		context_dict['category'] = category
	except Category.DoesNotExist:
		# We arrive here if no category is found
		# Don't do anything, because the template displays "no category" if nothing
		pass

	return render_to_response('rango/category.html', context_dict, context)


def add_category(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = forms.CategoryForm(request.POST)

		if form.is_valid():
			# If the form is valid, write to db
			form.save(commit=True)

			# Return to homepage
			return index(request)
		else:
			print form.errors
	else:
		# If the request was not POST, display the form to enter details
		form = forms.CategoryForm()

	return render_to_response('rango/add_category.html', {'form': form}, context)