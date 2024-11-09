from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home_page"),
    path("goodprice/", good_price_sellers, name="good_price_sellers"),
    path("expensive/", expensive_sellers, name="expensive_sellers"),
    path("stats/<int:seller_id>/", seller_orders_count, name="seller_orders_count"),
]

