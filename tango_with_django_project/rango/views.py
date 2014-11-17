# from django.http import HttpResponse
from models import Category
from models import Page
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms


def decode_url(url):
	"""
	Replaces spaces with underscores for translating category name to/from URL
	It can't account for category names with underscores at the moment,
	but that may not be a problem
	:param url: requested url to decode
	:return: url with underscores
	"""
	# url = url.replace('_', ' ')
	url = url.replace(' ', '_')
	return url


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
	for _category in category_list:
		_category.url = decode_url(_category.name)

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
	print category_name_url
	category_name = decode_url(category_name_url)

	context_dict = {'category_name': category_name,
					'category_name_url': category_name_url}

	try:
		# Can we find a category with the new given name?
		# If not, the .get() method raises DoesNotExist exception
		_category = Category.objects.get(name=category_name)

		# Retrieve all associated pages
		# .filter method returns >= 1 model instance
		pages = Page.objects.filter(category=_category)

		# Add results list to template context
		context_dict['pages'] = pages

		# We also add the category object from the database to the context directory
		# We'll use this in the template to verify that the category exists
		context_dict['category'] = _category
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


def add_page(request, category_name_url):
	context = RequestContext(request)

	category_name = decode_url(category_name_url)

	if request.method == 'POST':
		form = forms.PageForm(request.POST)

		if form.is_valid():
			# We can't commit immediately this time, cause not all fields are populated
			page = form.save(commit=False)

			# Retrieve associated category object so we can add it
			try:
				cat = Category.objects.get(name=category_name)
				page.category = cat
			except Category.DoesNotExist:
				# If the category doesn't exist, return add_category form to indicate
				form = forms.CategoryForm()
				return render_to_response('rango/add_category.html', {'form': form}, context)

			# Create number of views and likes
			page.views = 0
			page.likes = 0

			# Now we can save
			page.save()

			# Now that the page is saved, return the category instead
			return category(request, category_name_url)

		else:
			print form.errors

	else:
		form = forms.PageForm()

	return render_to_response('rango/add_page.html',
		{'category_name_url': category_name_url,
		 'category_name': category_name, 'form': form},
		context)
