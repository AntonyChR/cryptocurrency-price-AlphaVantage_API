import requests

def get_info(url, time_interval, crypto, physical_c, key):
    args = {
            "function": time_interval,
            "symbol"  : crypto,
            "market"  : physical_c,
            "apikey"  : key
            }
    response = requests.get(url, params = args)

    if response.status_code == 200:
        return response.json()

    print("request error")

def filter_data():
    pass
