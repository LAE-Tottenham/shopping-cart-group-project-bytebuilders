
#CURRENCY EXCHANGE FUCNCTION - DANIEL + VAHID

def check_currency_exists(exchange_rates):
    currency = input("Please enter the currency that you would like to convert into: ").upper()
    if currency in exchange_rates: 
        return currency
    else: 
        return True

def currency_convert(currency, exchange_rates, shoppingPrice):
    original_amount = shoppingPrice
    while float(original_amount) < 10.0 or float(original_amount) > 1000.0:
        original_amount = input("Please enter the amount that you'd like to convert: ") 

    new_amount = float(original_amount) * exchange_rates[currency]
    
    
    return round(new_amount, 2)

def view_rates(exchange_rates):
    for value in exchange_rates:
        print(f'{value}: '+ str("{:.2f}".format(exchange_rates[value])))

def price_output(exchange_rates, shoppingPrice):
    currency = check_currency_exists(exchange_rates)

    while True: 
        if currency == True: 
            currency = check_currency_exists(exchange_rates)
        else:
            break

    amount = str(currency_convert(currency, exchange_rates, shoppingPrice))

    if amount[-2] == ".":
        amount += "0"

    return amount, currency