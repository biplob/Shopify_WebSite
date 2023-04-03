import requests
import json
import pandas as pd

url = 'https://www.adoredvintage.com/products.json?limit=2000&page1'

res = requests.get(url)

data = res.json()

data_list = []

for product in data['products']:
    id = product['id']
    title = product['title']
    product_description = product['body_html']
    vendor = product['vendor']
    product_type = product['product_type']
    tags = product['tags']

    for variant in product['variants']:
        product_id = variant['product_id']
        sku = variant['sku']
        shipping = variant['requires_shipping']
        available = variant['available']
        price = variant['price']
        position = variant['position']

    for image in product['images']:
        try:
            image_src = image['src']
        except:
            image_src = None



    product_items = {
        'id': id,
        'title': title,
        'product_description': product_description,
        'vendor': vendor,
        'product_type': product_type,
        'tags': tags,
        'product_id': product_id,
        'sku': sku,
        'shipping': shipping,
        'available': available,
        'price': price,
        'position':position

    }

    data_list.append(product_items)


datas = pd.DataFrame(data_list, columns=['id', 'title', 'product_description', 'vendor', 'product_type', 'tags', 'product_id',
                                         'sku', 'shipping', 'available', 'price', 'position'])

datas.to_csv('Adoredivintage.csv', index=False, encoding='utf-8')
