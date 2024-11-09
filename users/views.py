from django.shortcuts import render
from .models import Seller
from .queryset import *

def home_page(request):
    sellers = get_sellers_with_more_than_one_product()
    return render(request, 'home_page.html', {'sellers_count':len(sellers)})

    
def good_price_sellers(request):
    seller = get_sellers_with_good_price()
    return render(request, 'good_price_sellers.html',{'sellers':seller})
    
def expensive_sellers(request):
    seller = get_seller_with_max_price()
    return render(request,'expensive_sellers.html',{'sellers':seller})
    
def seller_orders_count(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    orders_count = sum_of_orders_in_30_days(seller)
    if not orders_count:
        orders_count = "0"
    return render(request, 'seller_orders_count.html', {'sales_count': orders_count, 'seller_name': seller.username })