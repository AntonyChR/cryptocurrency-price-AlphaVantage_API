from pandas import read_csv
#"Intraday": "CRYPTO_INTRADAY",
time_series = {
                "Daily"  : "DIGITAL_CURRENCY_DAILY",
                "Weekly" : "DIGITAL_CURRENCY_WEEKLY",
                "Monthly": "DIGITAL_CURRENCY_MONTHLY"
                }
#This function returns the code and names of the cryptocurrencies and their 
#price in physical currency
def cryptocurrencies(path: str) -> [list, list]:
    df = read_csv(path)
    return list(df["currency name"]),list(df["currency code"])

