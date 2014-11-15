import os


def populate ():
	python_cat = add_cat("Python")

	add_page(cat = python_cat,
			 title = "Official Python Tutorial",
			 url = "http://docs.python.org/2/tutorial/",
			 likes = 64,
			 views = 128)

	add_page(cat = python_cat,
			 title = "How to Think like a Computer Scientist",
			 url = "http://www.greenteapress.com/thinkpython/",
			 likes = 64,
			 views = 128)

	add_page(cat = python_cat,
			 title = "Learn Python in 10 Minutes",
			 url = "http://www.korokithakis.net/tutorials/python/",
			 likes = 64,
			 views = 128)

	django_cat = add_cat("Django")

	add_page(cat = django_cat,
			 title = "Official Django Tutorial",
			 url = "https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
			 likes = 50,
			 views = 123)

	add_page(cat = django_cat,
			 title = "Django Rocks",
			 url = "http://www.djangorocks.com/",
			 likes = 482,
			 views = 103)

	add_page(cat = django_cat,
			 title = "How to Tango with Django",
			 url = "http://www.tangowithdjango.com/",
			 likes = 75,
			 views = 101)

	frame_cat = add_cat("Other Frameworks")

	add_page(cat = frame_cat,
			 title = "Bottle",
			 url = "http://bottlepy.org/docs/dev/",
			 likes = 10,
			 views = 5)

	add_page(cat = frame_cat,
			 title = "Flask",
			 url = "http://flask.pocoo.org",
			 likes = 74,
			 views = 28)


def add_page(cat, title, url, likes = 0, views = 0):
	p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views, likes=likes)[0]
	""" get_or_create() checks to see if the object exists already, returns (object, created)
	where object refers to the created object if nothing's found, and created is a bool describing
	whether the method created an object or not
	"""
	return p


def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c


if __name__ == '__main__':
	print("Starting Rango population script...")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from rango.models import Category, Page
	populate()