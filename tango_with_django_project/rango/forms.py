from django import forms
import models


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	# An inline class to provide additional info on the form
	class Meta:
		# Link form request and db model
		model = models.Category


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		# If url is not empty and doesn't start with 'http://,' prepend
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
		#change
		return cleaned_data

	class Meta:
		# Provide an association between the ModelForm and a model (Page)
		model = models.Page

		# List of fields to include in the form
		fields = ('title', 'url', 'views')