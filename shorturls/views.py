from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.conf import settings
from .models import *
from django.shortcuts import redirect
import requests
import time
from django.views.decorators.csrf import csrf_exempt
from urlparse import urlparse
from random import randint

class LinkCreate(CreateView):
	model = Link
	fields = ["url"]

	def form_valid(self, form):
		prev = Link.objects.filter(url=form.instance.url)
		if prev:
			return redirect("link_show", pk=prev[0].pk)
		return super(LinkCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(LinkCreate, self).get_context_data(**kwargs)
		# Passing site_url to display domain base
		context['site_url'] = settings.SITE_URL
		return context

class LinkShow(DetailView):
	model = Link
	def get_context_data(self, **kwargs):
		context = super(LinkShow, self).get_context_data(**kwargs)
		context['site_url'] = settings.SITE_URL
		return context


class RedirectToLongURL(RedirectView):

	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		short_url = kwargs["short_url"]
		return Link.expand(short_url)
