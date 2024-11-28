import requests

url = 'https://marketdata.tradermade.com/api/v1/live?api_key=ceWoy_Kfrqq42dUehyOY&currency=GBPUSD,GBPEUR,GBPCHF,GBPJPY,GBPCAD'
response = requests.get(url)
currency_response = requests.get(url).json()["quotes"]

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

def check_currency_exists(currency):

 if currency in currency_dict:
        return True
 else:
        return False
def currency_convert():
    currency = input(f"What would you like to convert to? our current rates against the GBP are {currency_dict}: ").upper()
    while currency not in currency_dict:
        print("That is not a supported currency.")
        currency = input(f"What would you like to convert to? our current rates against the GBP are {currency_dict}: ").upper()

    if check_currency_exists(currency) == True:
         amount = float(input(f"What amount would you like to convert to {currency}: "))
         while float(amount) < 10.0 or float(amount) > 1000.0:
            print("amount must be > £10 and < £1000.")
            amount = float(input(f"What amount would you like to convert to {currency}: "))
    convertedCurrency = amount*float(currency_dict[currency])
    return f"{convertedCurrency:.2f}"
print(currency_convert())  