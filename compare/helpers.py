# import requests
#
# def fetch_flipkart_products(search_query):
#     api_key = '<YOUR_FLIPKART_API_KEY>'
#     base_url = 'https://api.flipkart.com/search'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }
#
#     params = {
#         'q': search_query,
#     }
#
#     response = requests.get(base_url, headers=headers, params=params)
#     data = response.json()
#
#     # Process and extract relevant product details from Flipkart API response
#     product_data = []
#     for item in data['products']:
#         product = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url'],
#         }
#         product_data.append(product)
#
#     return product_data
#
# def fetch_amazon_products(search_query):
#     api_key = '<YOUR_AMAZON_API_KEY>'
#     base_url = 'https://api.amazon.com/search'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }
#
#     params = {
#         'q': search_query,
#     }
#
#     response = requests.get(base_url, headers=headers, params=params)
#     data = response.json()
#
#     # Process and extract relevant product details from Amazon API response
#     product_data = []
#     for item in data['products']:
#         product = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url'],
#         }
#         product_data.append(product)
#
#     return product_data

# def fetch_Myntra_products(search_query):
#     api_key = '<YOUR_MYTRA_API_KEY>'
#     base_url = 'https://api.myntra.com/search'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }
#
#     params = {
#         'q': search_query,
#     }
#
#     response = requests.get(base_url, headers=headers, params=params)
#     data = response.json()
#
#     # Process and extract relevant product details from Myntra API response
#     product_data = []
#     for item in data['products']:
#         product = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url'],
#         }
#         product_data.append(product)
#
#     return product_data
#
# def fetch_Bigbasket_products(search_query):
#     api_key = '<YOUR_BIGBASKET_API_KEY>'
#     base_url = 'https://api.bigbasket.com/search'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }
#
#     params = {
#         'q': search_query,
#     }
#
#     response = requests.get(base_url, headers=headers, params=params)
#     data = response.json()
#
#     # Process and extract relevant product details from Bigbasket API response
#     product_data = []
#     for item in data['products']:
#         product = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url'],
#         }
#         product_data.append(product)
#
#     return product_data
#
# def fetch_Meesho_products(search_query):
#     api_key = '<YOUR_MEESHO_API_KEY>'
#     base_url = 'https://api.meesho.com/search'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }
#
#     params = {
#         'q': search_query,
#     }
#
#     response = requests.get(base_url, headers=headers, params=params)
#     data = response.json()
#
#     # Process and extract relevant product details from Meesho API response
#     product_data = []
#     for item in data['products']:
#         product = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url'],
#         }
#         product_data.append(product)
#
#     return product_data

import requests


def fetch_flipkart_products(search_query):
    api_key = '<YOUR_FLIPKART_API_KEY>'
    base_url = 'https://api.flipkart.com/search'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    params = {
        'q': search_query,
    }

    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

    # Process and extract relevant product details from Flipkart API response
    product_data = []
    for item in data['products']:
        product = {
            'name': item['name'],
            'price': item['price'],
            'url': item['url'],
        }
        product_data.append(product)

    return product_data


def fetch_amazon_products(search_query):
    api_key = '<YOUR_AMAZON_API_KEY>'
    base_url = 'https://api.amazon.com/search'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    params = {
        'q': search_query,
    }

    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

    # Process and extract relevant product details from Amazon API response
    product_data = []
    for item in data['products']:
        product = {
            'name': item['name'],
            'price': item['price'],
            'url': item['url'],
        }
        product_data.append(product)

    return product_data
