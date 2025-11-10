import requests
import pprint

url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
api_key = "00d1931d506b433e93218b2d5ea57bd4"

params = {
    "key":api_key,
    "outputType": "JSON",
    "rt": "red"
}

response = requests.get(url, params=params)

pprint.pprint(response.json())