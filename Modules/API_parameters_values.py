from pandas import read_csv
time_series = {"Intraday": "CRYPTO_INTRADAY",
                "Daily"  : "DIGITAL_CURRENCY_DAILY",
                "Weekly" : "DIGITAL_CURRENCY_WEEKLY",
                "Monthly": "DIGITAL_CURRENCY_MONTHLY"
                }
def cryptocurrencies(path: str) -> [list, list]:
    df = read_csv(path)
    return list(df["currency name"]),list(df["currency name"])




