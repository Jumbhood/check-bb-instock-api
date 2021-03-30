from product_list import GTX3060TI, GTX3070, GTX3080, GTX3090
from scrape import scrape, check_stock, create_message
import requests
import json

slack_url = "INSERT_URL"
slack_header = {'Content-type': 'application/json'}

for g60 in GTX3060TI:
    data = scrape(g60)
    result = check_stock(data)
    if result == False:
        print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
    else:
        text = create_message(data)
        myobj = {'text' : text}
        r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
        print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))

for g70 in GTX3070:
    data = scrape(g70)
    result = check_stock(data)
    if result == False:
        print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
    else:
        text = create_message(data)
        myobj = {'text' : text}
        r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
        print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))

for g80 in GTX3080:
    data = scrape(g80)
    result = check_stock(data)
    if result == False:
        print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
    else:
        text = create_message(data)
        myobj = {'text' : text}
        r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
        print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))

for g90 in GTX3090:
    data = scrape(g90)
    result = check_stock(data)
    if result == False:
        print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
    else:
        text = create_message(data)
        myobj = {'text' : text}
        r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
        print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))

# test = ['10416248']
# for t in test:
#     data = scrape(t)
#     result = check_stock(data)
#     if result == False:
#         print("[ INFO ] - {} - {}".format(data['name'], "Not in Stock"))
#     else:
#         text = create_message(data)
#         myobj = {'text' : text}
#         r = requests.post(slack_url, data = json.dumps(myobj), headers = slack_header)
#         print("[ ALERT ] - {} - {}".format(data['name'], "In Stock"))