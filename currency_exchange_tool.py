import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    'CAD' : 1.80,
    'CHF' : 1.12,
    'JPY': 194.43
}

def check_currency_exists():
    currency = input("Please enter the currency that you would like to convert into: ").upper()
    if currency in exchange_rates: 
        return currency
    else: 
        return True
        

def currency_convert(currency):
    # your code here
    original_amount = input("Please enter the amount that you'd like to convert: ")
    while float(original_amount) < 10.0 or float(original_amount) > 1000.0:
        original_amount = input("Please enter the amount that you'd like to convert: ") 

    new_amount = float(original_amount) * exchange_rates[currency]
    
    
    return round(new_amount, 2)

print(exchange_rates)

currency = check_currency_exists()

while True: 
    if currency == True: 
        currency = check_currency_exists()
    else:
        break

amount = str(currency_convert(currency))

if amount[-2] == ".":
    amount += "0"

print("Your new amount in " + currency + " is " + str(amount))

