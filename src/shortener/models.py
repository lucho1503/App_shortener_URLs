from django.conf import settings
from django.db import models
from django_hosts.resolvers import reverse
import string
import random


from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):
		qs = KirrURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "new codes made: {i}".format(i=new_codes)

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)#unique=True) # everytime the model is saved	
	updated = models.DateTimeField(auto_now=True) # when model is created
	timestamp = models.DateTimeField(auto_now_add=True) # when model is created
	active = models.BooleanField(default=True)

	objects = KirrURLManager()


	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)

	#def my_save(self):


	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={"shortcode": self.shortcode}, host="www", scheme="http", port="8000")
		return url_path