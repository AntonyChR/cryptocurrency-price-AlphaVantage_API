import requests

# makes a query to the Alpha vantage API
def get_info(url, time_interval, crypto, physical_c, key) -> dict:
    print(f"getting: {crypto} -> {physical_c} [{time_interval}]")
    args = {
            "function": time_interval,
            "symbol"  : crypto,
            "market"  : physical_c,
            "apikey"  : key
            }
    response = requests.get(url, params = args)
    """
    in particular the Alpha Vantage API even if an 
    error has occurred returns the code 200, WTF ?! XD
    """
    if response.status_code == 200:
        return response.json()

    print("request error")

# of the information, only the closing price is returned
def filter_data(data: dict, interval: str, curr:str) -> [list, list]:
    t_series = f"Time Series (Digital Currency {interval})"
    op       = f"4a. close ({curr})" 
    try:
        date = list(data[t_series].keys())
        date.reverse()
        price = [float(data[t_series][d][op]) for d in date]

        return date, price
    except KeyError as err:
        print(f"The Alpha Vantage API does not return the information about this cryptocurrency")





    

