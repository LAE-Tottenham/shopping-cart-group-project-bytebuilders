
#VAHID + DANIEL CURRENCY EXCHANGE FUNCTION

import requests

url = 'https://marketdata.tradermade.com/api/v1/live?api_key=ceWoy_Kfrqq42dUehyOY&currency=GBPUSD,GBPEUR,GBPCHF,GBPJPY,GBPCAD'
response = requests.get(url)
currency_response = requests.get(url).json()["quotes"]

def exchangeRates():
    if response.status_code == 200:

            usd = response.json()["quotes"][0]["mid"]
            eur = response.json()["quotes"][1]["mid"]
            chf = response.json()["quotes"][2]["mid"]
            jpy = response.json()["quotes"][3]["mid"]
            cad = response.json()["quotes"][4]["mid"] 
    currency_dict={
        "USD" : f"{usd}",
        "EUR" : f"{eur}", 
        "CAD" : f"{cad}", 
        "CHF" : f"{chf}", 
        "JPY" : f"{jpy}",  
        }
    return currency_dict

def check_currency_exists(currency, currency_dict):

 if currency in currency_dict:
        return True
 else:
        return False
 
def currency_convert(currency_dict, totalPrice):
    print("What would you like to convert to? our current rates against the GBP are:")
    for differentCurrency in currency_dict:
        print(f"{differentCurrency}: {currency_dict[differentCurrency]}")
    print("")
    currency = input().upper()
    while currency not in currency_dict:
        print("That is not a supported currency.")
        print("What would you like to convert to? our current rates against the GBP are:")
        for differentCurrency in currency_dict:
             print(f"{differentCurrency}: {currency_dict[differentCurrency]}")
        print("")
        currency = input().upper()
    if check_currency_exists(currency, currency_dict) == True:
        if float(totalPrice) < 10.0 or float(totalPrice) > 1000.0:
            print("amount must be > £10 and < £1000.")
        else:
            convertedCurrency = totalPrice*float(currency_dict[currency])
    return convertedCurrency, currency

def view_rates(exchange_rates):
    print(exchange_rates)