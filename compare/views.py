import requests
from django.core.exceptions import ObjectDoesNotExist

from .helpers import fetch_flipkart_products, fetch_amazon_products
from .models import Product, ShoppingSite
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def search_products(request):
    if request.method == 'Post':
        search_query = request.POST.get('search')

        # Make API requests to Flipkart and Amazon
        # flipkart_data = fetch_flipkart_products(search_query)
        # amazon_data = fetch_amazon_products(search_query)
        #
        # # To Save the fetched product data to the database
        # for item in flipkart_data:
        #     Product.objects.create(
        #         name=item['name'],
        #         price=item['price'],
        #
        #     )
        # for item in amazon_data:
        #     Product.objects.create(
        #         name=item['name'],
        #         price=item['price'],
        #
        #     )

        # Retrieve the saved product data from the database
        products = Product.objects.filter(name__icontains=search_query)

        context = {
            'products': products,
        }

        return render(request, 'product_search.html', context)

    return render(request, 'index.html')


def search(request):
    if request.method == 'POST':
        print("request.data: ", request)
        # print("request_url: ", request.build_absloute_uri())
        print(request.POST)
        search_query = request.POST.get('search_query')
        print("search_query: ", search_query)
        # amazon_url = f'https://www.amazon.com/s?k={search_query}'
        # flipkart_url = f'https://www.flipkart.com/s?k={search_query}'

        # Create a new product object and save it
        try:
            product = Product.objects.get(name__iexact=search_query)
            products = ShoppingSite.objects.filter(product=product)

        except ObjectDoesNotExist:
            # product = Product.objects.create(name=search_query, price=0)  # Replace 'price' with the actual price value
            return render("Not Found")
            pass
        return render(request, 'index.html', {'products': products})

    return render(request, 'index.html')
