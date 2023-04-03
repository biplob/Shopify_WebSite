import requests
import json
import pandas as pd

url = 'https://www.tentree.ca/products.json?limit=1000&page1'

response = requests.get(url)
data = response.json()

product_list = []

for product in data['products']:
    title = product['title']
    handle = product['handle']
    description = product['body_html']
    prublish_date = product['published_at']
    created_date = product['created_at']
    product_type = product['product_type']
    tags = product['tags']


    for variant in product['variants']:
        product_id = variant['product_id']
        variant_title = variant['title']
        sku = variant['sku']
        price = variant['price']
        available = variant['available']
        option1 = variant['option1']
        grams = variant['grams']


    for image in product['images']:
        try:
            imagesrc = image['src']

        except:
            imagesrc = None

        # print(imagesrc)

    product_item = {
        'product_id': product_id,
        'title': title,
        'variant_title': variant_title,
        'handle': handle,
        'description': description,
        'prublish_date': prublish_date,
        'created_date': created_date,
        'product_type': product_type,
        'tags': tags,
        'sku': sku,
        'price': price,
        'available': available,
        'option1': option1,
        'grams': grams,
        'image': imagesrc

    }
    product_list.append(product_item)

df = pd.DataFrame(product_list, columns=['product_id', 'title', 'variant_title', 'handle', 'description', 'prublish_date',
                                         'created_date', 'product_type', 'tags', 'sku', 'price', 'available',
                                         'grams', 'image'])


df.to_csv('Tentree.csv', index=False, encoding='utf-8')

