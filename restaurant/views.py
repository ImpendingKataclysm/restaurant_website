from django.shortcuts import render
from django.views import generic
from datetime import datetime

from .models import Item, TYPE, Location, Reservation
from .forms import ReservationForm


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


class LocationList(generic.ListView):
    queryset = Location.objects.order_by("city")
    template_name = "contact.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LocationDetail(generic.DetailView):
    model = Location
    template_name = "location_detail.html"


def reserve(request):
    restaurant_locs = Location.objects.order_by("city")
    context = {"locations": []}

    for loc in restaurant_locs:
        context["locations"].append(loc)

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            party_name = form.cleaned_data["party_name"]
            party_size = form.cleaned_data["party_size"]
            contact_phone = form.cleaned_data["contact_phone"]
            location = form.cleaned_data["location"]
            date_reserved = form.cleaned_data["date_reserved"]
            time_reserved = form.cleaned_data["time_reserved"]
            booking_date = datetime.now()

            for loc in context["locations"]:
                loc_str = f"{loc.unit_no} {loc.street} {loc.city}, {loc.province}"

                if loc_str == location:
                    Reservation.objects.create(party_name=party_name,
                                               party_size=party_size,
                                               contact_phone=contact_phone,
                                               location=loc,
                                               date_reserved=date_reserved,
                                               time_reserved=time_reserved,
                                               booking_date=booking_date)
        else:
            print('not valid:')
            print(form.errors)

    return render(request, "reserve.html", context)
