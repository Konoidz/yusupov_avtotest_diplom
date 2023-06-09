import configuration
import requests

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=track_number)