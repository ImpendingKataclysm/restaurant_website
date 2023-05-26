from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
    ("drinks", "Drinks")
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)


class Item(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=200, choices=TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    unit_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=6)
    province = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.unit_no} {self.street} {self.city}, {self.province}"


class Reservation(models.Model):
    party_name = models.CharField(max_length=1000)
    party_size = models.IntegerField()
    contact_phone = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_reserved = models.DateField()
    time_reserved = models.TimeField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.party_name}, {self.date_reserved}"
