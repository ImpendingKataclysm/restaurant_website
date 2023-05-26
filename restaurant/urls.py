from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('menu/', views.MenuList.as_view(), name='menu'),
    path('item/<int:pk>', views.MenuItemDetail.as_view(), name='menu_item'),
    path('contact/', views.LocationList.as_view(), name='contact'),
    path('location/<int:pk>', views.LocationDetail.as_view(), name='location'),
    path('reserve/', views.reserve, name='reservation')
]
