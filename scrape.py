import requests
from fake_useragent import UserAgent
import json

def scrape(product_id):
    api_url = 'https://www.bestbuy.ca/api/v2/json/product/'
    full_url = api_url + product_id
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
        response = response.json()
        result = {
            'name' : response['name'],
            'isPurchasable' : response['isPurchasable'],
            'productUrl' : response['productUrl'],
            'salePrice' : response['salePrice']
        }
        return result
    else:
        return False

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
    sale_price = data['salePrice']
    text = 'Hey <!everyone>! Seems like `{}` is in stock now for `{} CAD`, check :alert:<{}|*Purchase Link*>:alert:'.format(name, sale_price, product_url)
    return text

def send_request(card_list, slack_url, slack_header):
    for card in card_list:
        data = scrape(card)
        if data == False:
            print("[ ERROR ] - Can't connect to the server!")
        else:
            result = check_stock(data)
            if result == False:
                print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
            elif result == True:
                text = create_message(data)
                myobj = {'text' : text}
                r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
                print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))
            else:
                print("[ ALERT ] - {} - {}".format(data['name'], "Unknown Status"))