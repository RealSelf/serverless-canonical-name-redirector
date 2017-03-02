""" This function takes any HTTP request, and sends back a 301 to 
https://www.realself.com

"""
import json

def redirect(event, context):
    print("%s" % (json.dumps(event)))
    response = {
        "statusCode": 301,
        "headers": {
           "Location": "https://www.realself.com/"
         },
        "body": ""
    }
    return response
