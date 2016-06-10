from django.db import models
from django.core.urlresolvers import reverse
from hashids import Hashids
hashids = Hashids()

class Link(models.Model):
	url = models.URLField()

	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})

	# Encodes Url
	def shorten(self):
		l, _ = Link.objects.get_or_create(url=self.url)
		return str(hashids.encrypt(l.pk))

	# Decodes short url
	@staticmethod
	def expand(slug):
		dirty_str = str(hashids.decrypt(slug))
		clean_id = dirty_str.strip("(,)")
		link_id = int(clean_id)
		l = Link.objects.get(pk=link_id)
		return l.url

	def short_url(self):
		return reverse("redirect_short_url",
                   kwargs={"short_url": Link.shorten(self)})
                   
	def __unicode__(self):
		return self.url
                   
class Auth(models.Model):
    authc = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    mail = models.CharField(max_length=10);
    rmail = models.CharField(max_length=10)
    def __unicode__(self):
        return self.authc