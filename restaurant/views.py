
from os import listdir
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
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
        images = listdir('restaurant/static/images/')
        context['images'] = [f"images/{image}" for image in images if image.startswith('menu')]
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

                    email_subject = "Reservation"
                    message = f"""
                                Thank you for your reservation at Best Restaurant for {date_reserved} at {time_reserved}!
                                Reservation details:
                                Date: {date_reserved}
                                Time: {time_reserved}
                                Party Name: {party_name}
                                Party Size: {party_size}
                                Contact Phone: {contact_phone}
                                Location Address: {loc}
                                """

                    # send_email(email_subject, message, email)

                    success_message = f"Reservation for {date_reserved} at {time_reserved} successful. Check your email for more details."
                    messages.success(request, success_message)
        else:
            messages.error(request, "Sorry, there was a problem processing your form. Please try again.")

    return render(request, "reserve.html", context)
