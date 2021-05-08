import requests

def get_info(url, time_interval, crypto, physical_c, key) -> dict:
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

def filter_data(data: dict, interval: str, curr:str) -> [list, list]:
    t_series = f"Time Series (Digital Currency {interval})"
    op       = f"4a. close ({curr})" #work with the closing price
    date = list(data[t_series].keys())
    date.reverse()
    price = [float(data[t_series][d][op]) for d in date]

    return date, price





    

