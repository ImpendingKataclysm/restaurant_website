from django.shortcuts import render
from django.views import generic

from .models import Item


class HomePage(generic.TemplateView):
    template_name = "index.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_added")
    template_name = "menu.html"
