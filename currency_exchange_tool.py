import requests
currency_dict = {
    "GBP": 1,
    "EUR": 1.20,
    "USD": 1.31,
    "CAD": 1.80,
    "CHF": 1.12,
    "JPY": 194.66
}
original_c = "GBP"
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
    convertedCurrency = amount*currency_dict[currency]
    return f"{convertedCurrency:.2f}"
print(currency_convert())   
