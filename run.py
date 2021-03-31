from product_list import GTX3060TI, GTX3070, GTX3080, GTX3090
from scrape import scrape, check_stock, create_message, send_request
import requests
import json

gitslack_url = "INSERT_URL"
slack_header = {'Content-type': 'application/json'}

if __name__ == '__main__':
    send_request(GTX3060TI, slack_url, slack_header)
    send_request(GTX3070, slack_url, slack_header)
    send_request(GTX3080, slack_url, slack_header)
    send_request(GTX3090, slack_url, slack_header)

    # Test list, put any product id in the list for testing purposes
    #testlist = ['12383793']
    #send_request(testlist, slack_url, slack_header)