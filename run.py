from product_list import GTX3060TI, GTX3070, GTX3080, GTX3090
from scrape import *
import time

slack_url = "INSERT_URL"
slack_header = {'Content-type': 'application/json'}

if __name__ == '__main__':
    instock_list = []
    while True:
        send_request(GTX3060TI, slack_url, slack_header, instock_list)
        send_request(GTX3070, slack_url, slack_header, instock_list)
        send_request(GTX3080, slack_url, slack_header, instock_list)
        send_request(GTX3090, slack_url, slack_header, instock_list)

        # Test list, put any product id in the list for testing purposes
        #testlist = ['12383793']
        #send_request(testlist, slack_url, slack_header, instock_list)

        time.sleep(5)