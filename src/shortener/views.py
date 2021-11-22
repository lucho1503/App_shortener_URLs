from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404

from analytics.models import ClickEvent

from .models import KirrURL
from .forms import SubmitUrlForm

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "OwlByt.com",
			"form": the_form
		}
		return render(request, "shortener_templates/home.html", context) # try django


	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "OwlByt.co",
			"form": form
		}
		template = "shortener_templates/home.html"

		if form.is_valid():
			#print(form.cleaned_data)
			new_url = form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object" : obj,
				"created": created,
			}
			if created:
				template = "shortener_templates/success.html"
			else:
				template = "shortener_templates/ya_existe.html"
	
		return render(request, template, context)
# Create your views here.
#def kirr_redirect_view(request, shortcode=None, *args, **kwargs): # functions based view
#	obj = get_object_or_404(KirrURL, shortcode=shortcode)
#	return HttpResponseRedirect(obj.url)


class UrlRedirectView(View): # class based viewiew
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		# saved item
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)


"""

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): # functions based view
	#print(args)
	#print(kwargs)
	
#	try:
#		obj = KirrURL.objects.get(shortcode=shortcode)
#	except:
#		obj = KirrURL.objects.all().first()

	obj = get_object_or_404(KirrURL, shortcode=shortcode)

#	obj_url = None
#	qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
#	if qs.exists() and qs.count() == 1:
#		obj = qs.first()
#		obj_url = obj.url
	return HttpResponseRedirect(obj.url)

"""