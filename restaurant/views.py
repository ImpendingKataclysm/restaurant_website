from django.shortcuts import render
from django.views import generic

from .models import Item, TYPE


class HomePage(generic.TemplateView):
    template_name = "index.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_added")
    template_name = "menu.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
