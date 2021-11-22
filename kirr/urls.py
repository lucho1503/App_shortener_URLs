"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from shortener.views import UrlRedirectView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('view-1', kirr_redirect_view),
    #path('view-2', Kirr_CVB_view.as_view()),
    re_path(r'^$', HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$', UrlRedirectView.as_view(), name="scode"),
]
