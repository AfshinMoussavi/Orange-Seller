from users.models import Seller , Product, Order
from django.db.models import Count, Q, F, Max, Avg,Func,Sum
from django.utils import timezone
from datetime import timedelta, datetime
import jdatetime
from django.shortcuts import get_object_or_404

def get_sellers_with_more_than_one_product():
    """
    Retrieves sellers who have more than one product registered in the system.

    This function uses Django ORM to annotate each seller with the count of their associated products
    and filters the results to return only those sellers who have more than one product.

    Returns:
        QuerySet: A QuerySet of Seller objects who have more than one product.
    """
    sellers = Seller.objects.annotate(product_count=Count('product')).filter(product_count__gt=1)
    return sellers

def get_mean_weight_of_seller_products(seller):
    """
    Calculates the average weight of products registered by a specific seller.

    This function filters the products associated with the given seller and calculates the average weight
    using Django's `aggregate` function.

    Args:
        seller (Seller): The seller object for which the mean weight of products is calculated.

    Returns:
        float: The average weight of products for the specified seller, or `None` if no products exist.
    """
    mean_weight = Product.objects.filter(seller=seller).aggregate(avg_weight=Avg('weight'))['avg_weight']
    return mean_weight

def get_sellers_with_more_than_two_products_or_age_greater_than_30():
    """
    Retrieves sellers who either have more than two products registered in the system,
    or are older than 30 years.

    This function filters sellers based on two conditions: 
    - Sellers who have more than two products.
    - Sellers whose age is greater than 30 years (calculated from the `birth_date` field).

    Returns:
        QuerySet: A QuerySet of Seller objects who either have more than two products or are older than 30.
    """
    age = jdatetime.datetime.today().date()
    thirty_year = age.year - 30
    y_ago = jdatetime.datetime(year=thirty_year, month=age.month, day=age.day)
    sellers = Seller.objects.annotate(num_products=Count('product')).filter(Q(num_products__gt=2) | Q(birth_date__lt=y_ago))
    return sellers

def get_sellers_with_good_price():
    """
    Retrieves sellers who are considered "good sellers" based on product price-to-weight ratio
    and recent order delivery.

    A "good seller" is defined as a seller who:
    - Has a product price-to-weight ratio lower than 10,000.
    - Has delivered at least one product or order in the last 30 days.

    Returns:
        QuerySet: A QuerySet of Seller objects who are considered "good sellers" based on the criteria.
    """
    thirty_days_ago = timezone.now() - timedelta(days=30)
    
    sellers_with_good_price = Seller.objects.annotate(
        price_weight_ratio=Avg('product__price') / Avg('product__weight')
    ).filter(price_weight_ratio__lt=10000)

    sellers_with_recent_orders = sellers_with_good_price.filter(
        product__orders__due_date__gte=thirty_days_ago
    )

    return sellers_with_recent_orders

def get_seller_with_max_price():
    """
    Retrieves the seller with the most expensive product in the system.

    This function annotates each seller with the maximum price of their associated products and
    orders the sellers by the highest price, returning the seller with the highest-priced product.

    Returns:
        Seller: The seller who has the product with the highest price, or `None` if no sellers exist.
    """
    return Seller.objects.annotate(max_price=Max('product__price')).order_by('-max_price').first()

def sum_of_orders_in_30_days(seller):
    """
    Calculates the total number of orders delivered by a specific seller in the last 30 days.

    This function filters the orders for the given seller, considering only those delivered within
    the last 30 days, and sums the `count` field to return the total number of orders delivered.

    Args:
        seller (Seller): The seller object for which the total number of orders is calculated.

    Returns:
        int: The total number of orders delivered by the seller in the last 30 days.
    """
    thirty_days_ago = timezone.now() - timedelta(days=30)
    return Order.objects.filter(product__seller=seller, created_at__gte=thirty_days_ago).aggregate(sum_count=Sum('count'))['sum_count'] or 0
