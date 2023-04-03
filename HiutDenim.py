import requests
import json
import pandas as pd

url = 'https://hiutdenim.co.uk/products.json?limit=1000&page=1'

res = requests.get(url)

data = res.json()
# print(data)
data_all = []

for item in data['products']:
    id = item['id']
    title = item['title']
    handle = item['handle']
    product_description = item['body_html']
    publish_data = item['published_at']
    created_data = item['created_at']
    vendor = item['vendor']
    product_type = item['product_type']



    for variant in item['variants']:

        product_id = variant['product_id']
        product_title = variant['title']
        product_price = variant['price']
        shipping = variant['requires_shipping']
        sku = variant['sku']
        product_position = variant['position']

    for image in item['images']:
        try:
            src = image['src']

        except:
            src = None

        # print(src)

    product = {
        'Id': id,
        'Product_Id': product_id,
        'Title': title,
        'Product_Title': product_title,
        'Handle': handle,
        'Product_Description': product_description,
        'Publish_Data': publish_data,
        'Created_Data': created_data,
        'Vendor': vendor,
        'Product_Type': product_type,
        'Product_Price': product_price,
        'Shipping': shipping,
        'Sku': sku,
        'Product_Position': product_position,
        'Image': src

    }

    data_all.append(product)


data = pd.DataFrame(data_all, columns=['Id','Product_Id','Title','Product_Title','Handle','Product_Description', 'Publish_Data',
                                       'Created_Data','Vendor','Product_Type','Product_Price','Shipping',
                                       'Sku','Product_Position','Image'])

data.to_csv('HiutDenim.csv', index=False, encoding='utf-8')
print(data)




