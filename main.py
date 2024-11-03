import pyfiglet, shop_functions, time, currency_exchange_tool ; import importlib

#this keeps the code from breaking as it started being slow once the files got bigger
#it just reloads the files so it just uses the up-to-date version
importlib.reload(shop_functions)

shoppingPrice = 0.00
basket = []
currency = 'GBP'

shop_functions.clear_console()
print('Welcome to byteBuilders!\nBefore shopping with us, we require your postcode to calculate a shipping price.\nCharge rate is £8 per km. ')

area, longitude, latitude, destination = shop_functions.postcodeValidation()
shippingCost = shop_functions.distanceCalculation(longitude,latitude)

shoppingPrice += shippingCost

print('\nLoading shop...')
time.sleep(5)


exchange_rates = currency_exchange_tool.exchangeRates()


items = {
    'Bread': 1.20,
    'Milk': 1.15,
    'Chocolate': 1.00,
    'Sausages (X4)': 3.00,
    'Cheese': 3.75,
    'Baked Beans': 3.75,
    'Tomatoes (X6)': 0.95,
    'PG tips': 3.00,
    'Red Onions (X3)': 1.10,
    'Digestives': 3.50
}

shop_functions.clear_console()
shopping_cart_art = pyfiglet.figlet_format('byteBuilders')
print(shopping_cart_art)
input('Welcome to byteBuilders! Press ENTER to start shopping.\n')
shop_functions.start_shop(items, basket, shoppingPrice, exchange_rates, currency, shippingCost)