import requests
from fake_useragent import UserAgent
import subprocess
import json

def scrape(product_id):
    api_url = 'https://www.bestbuy.ca/api/v2/json/product/'
    full_url = api_url + product_id
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = requests.get(full_url, headers=headers).json()
    result = {
        'name' : response['name'],
        'isPurchasable' : response['isPurchasable'],
        'productUrl' : response['productUrl']
    }
    return result

def check_stock(data):
    is_purchasable = data['isPurchasable']
    if is_purchasable == True:
        return True
    else:
        return False

def create_message(data):
    name =  data['name']
    is_on_sale = data['isPurchasable']
    product_url = data['productUrl']
    text = 'Hey <!everyone>! Seems like `{}` is in stock now, check :alert:<{}|*Purchase Link*>:alert:'.format(name, product_url)
    return text