# import requests,json

# from flask import request_finished
# import json


# def get_quotes():
#     response = request_finished.get('http://quotes.stormconsultancy.co.uk/quotes.json')
#     if response.status_code == 200:
#         quote = response.json()
#         # print(quote)
#         return quote

import requests,json

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        # print(quote)
        return quote