
"""
This test checks if the Alpha Vantage API returns the correct information.

* It does not return information on the majority of 
  cryptocurrencies that appear on its official list

*In the free version, it only accepts 5 requests per minute and 500 per day.

"""

from Modules.API_parameters_values import *
from Modules.data import get_info
from pandas import DataFrame
from time import sleep

path = "./assets/digital_currency_list.csv"
url="https://www.alphavantage.co/query?"
interval = "DIGITAL_CURRENCY_DAILY"
name, code = cryptocurrencies(path)
llaves = ["UQ1U59KH7TUV3Y6J",
	"16KZ5JMCP2RS49ST",
        "NRX6UP693G7KCHNR",
        "MH1VZWD3TCM9DKTQ",
        "2UGTWC49WUCH13S5",
        "XQDU898R5AYO726B",
        "AEGL9P4WZJE0KS92",
        "0H8IETE3N2A7OYWW",
        "DHEQC98CQ5GB51BS",
	"HTA1JUYWAF8B0H6U"]
j = 0
num_k = len(llaves)
for i,sym in enumerate(code):

    if j == 4:
        sleep(75)
    j = 0 if j==num_k-1 else j+1
    APIkey = llaves[j]

    resp = get_info(url,interval,sym,"PEN", APIkey)
    keys = list(resp.keys())
    print(keys)
    try:
        if keys[0]=="Error Message":
            if sym == "BTC":
                print("--------error")
            name.remove(name[i])
            code.remove(code[i])
            print(f"{i}: {name[i]} -> CORRUPT")
        else:
            print(f"{i}: {name[i]} -> ACCEPT!!")
    except:
        pass
    
df = DataFrame({"currency code":code,"currency name":name})
df.to_csv("digital_currency_list.csv",index = False)

