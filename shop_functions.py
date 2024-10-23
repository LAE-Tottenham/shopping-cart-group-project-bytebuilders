
import os,platform,time,requests; import currency_exchange_tool; import importlib
importlib.reload(currency_exchange_tool)

#SHOPPING CART EXPERIENCE - ALIM + KATIE

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def loadPause():
    print('\nJust a sec...')
    time.sleep(0.5)


def change_currency(before_currency, new_currency):
    before_currency = new_currency
    return before_currency

def viewbasket(basket, shoppingPrice, currency):
    print('\n----------------------YOUR BASKET---------------------------\n')
    basketCount = 1
    for item in basket:
        print(str(basketCount)+ '.',item+'\n')
        basketCount += 1
    print('\nTotal Price (+ shipping):'+' '+ currency ,"{:.2f}".format(shoppingPrice))
    print('----------------------------------------------------------------')


def stop_shop(string):
    stop = False
    if string == 'STOP':
        stop = True
    return stop

def edit_basket(items, basket, shoppingPrice, currency):
    loadPause()
    clear_console()
    
    while True:
        clear_console()
        if len(basket) == 0:
            print("Your basket is empty.")
            break
        
        viewbasket(basket, shoppingPrice, currency)
        print('\nType CANCEL to stop editing.')
        removeItem = input('\nPick the number of an item to remove it: ')
        
        if removeItem == 'CANCEL':
            break
        
        if not removeItem.isdigit():
            continue

        removeIndex = int(removeItem) - 1
    
        if 0 <= removeIndex < len(basket):
            item = basket[removeIndex]
            removeConfirm = input(f'\nRemove {item}? (ENTER to confirm, or type any other character to cancel): ')
            
            if removeConfirm == '':
                basket.pop(removeIndex) 
                shoppingPrice -= items[item]
                print(f"\nItem removed: {item}")
                print(f"Total price: £{'{:.2f}'.format(shoppingPrice)}")
                continue
            else:
                print('Operation cancelled.\n')
        else:
            print("Invalid item number.")


def start_shop(items, basket, shoppingPrice, exchange_rates, currency):

    while True:
        clear_console()
        print('CATALOGUE:\n')
        itemNumbering = 1
        for value in items:
            print(str(itemNumbering) + '-->',str(value), ':', '£'+ str("{:.2f}".format(items[value])))
            itemNumbering +=1

        print('\nSelect an item number (1-10) and press ENTER to select the item.\nAlternatively, you can type STOP to stop shopping, or EDIT to view/edit your basket.\n\n')
        viewbasket(basket, shoppingPrice, currency)

        userChoice = input('\nPick an item: ')

        if stop_shop(userChoice):
            pay_selection(shoppingPrice, basket, items, exchange_rates, currency)
            return

        elif userChoice == 'EDIT':
            edit_basket(items, basket, shoppingPrice, currency)

        elif userChoice == '1' :
            basket.append('Bread')
            shoppingPrice += 1.20
            print('\nAdding item: Bread')
            loadPause()

        elif userChoice == '2' :
            basket.append('Milk')
            shoppingPrice += 1.15
            print('\nAdding item: Milk')
            loadPause()

        elif userChoice == '3' :
            basket.append('Chocolate')
            shoppingPrice += 1.00
            print('\nAdding item: Chocolate')
            loadPause()

        elif userChoice == '4' :
            basket.append('Sausages (X4)')
            shoppingPrice += 3.00
            print('\nAdding item: Sausages (X4)')
            loadPause()

        elif userChoice == '5' :
            basket.append('Cheese')
            shoppingPrice += 3.75
            print('\nAdding item: Cheese')
            loadPause()

        elif userChoice == '6' :
            basket.append('Baked Beans')
            shoppingPrice += 3.75
            print('\nAdding item: Baked Beans')
            loadPause()

        elif userChoice == '7' :
            basket.append('Tomatoes (X6)')
            shoppingPrice += 0.95
            print('\nAdding item: Tomatoes')
            loadPause()

        elif userChoice == '8' :
            basket.append('PG tips')
            shoppingPrice += 3.00
            print('\nAdding item: PG tips')
            loadPause()

        elif userChoice == '9' :
            basket.append('Red Onions (X3)')
            shoppingPrice += 1.10
            print('\nAdding item: Red Onions (X3)')
            loadPause()

        elif userChoice == '10' :
            basket.append('Digestives')
            shoppingPrice += 3.50
            print('\nItem added: Digestives')
            loadPause()

        else:
            continue



def shop_pay(basket, shoppingPrice, items, exchange_rates, currency):
    while True:
        clear_console()
        viewbasket(basket, shoppingPrice, currency)
        payConfirm = input(f'You have chosen to pay.\n\nEither:\n\n- Type PAY NOW to confirm payment\n- Press ENTER to cancel your payment\n- Type EDIT if you would still like to edit your basket\n- Type EXCHANGE if you would like to convert the price to another currency.\n\nYour input: ')
       
        if payConfirm == 'EDIT':
            edit_basket(items, basket, shoppingPrice, currency)
            continue

        elif payConfirm == 'EXCHANGE':
            
            while True:
                clear_console()
                continue_exchange = input(f'\nWARNING:\nYou will not be able to edit your basket once your currency has been converted.\nYou will simply go straight to payment.\n\nAre you sure you want to continue? (Y/N):  ')
                if continue_exchange == 'Y':
                #REMINDER: the pound sign doesnt yet change after a change of currency. fix.
                    if 10 <= shoppingPrice <= 1000:
                        print(' ')
                        currency_exchange_tool.view_rates(exchange_rates)
                        print(' ')
                        convertedMoney = currency_exchange_tool.price_output(exchange_rates, shoppingPrice)
                        shoppingPrice = float(convertedMoney[0])
                        currency = change_currency(currency, convertedMoney[1])
                        print(f'\nConverting to {currency}...')
                        time.sleep(2)
                        print(' ')
                        print("Your new amount in " + currency + " is " + str(shoppingPrice))
                        input('Press ENTER to continue to payment.')
                        print('Proceeding to payment...')
                        time.sleep(1)
                        pay_now(basket, shoppingPrice, currency)
                        return

                    else:
                        print(f'\nYour total price must be between {currency}10 and {currency}1000 in order to convert.')
                        input('Press ENTER to continue to payment.')
                        print('Proceeding to payment...')
                        time.sleep(1)
                        pay_now(basket, shoppingPrice, currency)
                        return
                    

                elif continue_exchange == 'N':
                    break
                continue
            
            

        elif payConfirm == 'PAY NOW':
            pay_now(basket, shoppingPrice, currency)
            return

        else:
            pay_selection(shoppingPrice, basket, items, exchange_rates, currency)
            return
            
def pay_now(basket, shoppingPrice, currency):
    clear_console()
    viewbasket(basket, shoppingPrice, currency)
    print('\nChecking details...\n')
    time.sleep(0.4)
    print('Communicating with bank...\n')
    time.sleep(2)
    print('Finalizing...\n')
    time.sleep(0.3)
    clear_console()
    print('Your payment has been accepted. Thank you for shopping with byteBuilders!')

    print('\n----------------------YOUR RECEIPT---------------------------\n')
    basketCount = 1
    for item in basket:
        print(str(basketCount)+ '.',item+'\n')
        basketCount += 1
    print('\nTotal Price (+ shipping):'+' '+ currency ,"{:.2f}".format(shoppingPrice))
    print('----------------------------------------------------------------\n\n')
    return
    

def pay_selection(shoppingPrice, basket, items, exchange_rates, currency):
    while True:
        clear_console()
        viewbasket(basket, shoppingPrice, currency)
        pay_choice = input(f'\nWould you like to pay (1) or continue shopping (2)?: ')
        if str(pay_choice) == '1':
            shop_pay(basket, shoppingPrice, items, exchange_rates, currency)
            return

        elif str(pay_choice) == '2':
            start_shop(items, basket, shoppingPrice , exchange_rates, currency)
            return

        else:
            continue


#------------------------------------------------------------------------------------------------

#DELIVERY PRICE CALCULATION USING API - KATIE

def postcodeValidation():
    valid=False
    while valid==False:
        try:
            valid=True
            postcode_raw = input("\nPlease enter your postcode: ")
            postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()

            area = postcode_resp['result']['admin_ward']
            longitude = postcode_resp['result']['longitude']
            latitude = postcode_resp['result']['latitude']
        except KeyError:
            valid=False
            print("Error. Please enter a valid postcode.")
    print(f"Area of Destination: {area}.\n")
    return area, longitude, latitude, postcode_raw


def distanceCalculation(longitude, latitude):
    results=(requests.get(f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={latitude},{longitude}&destinations=51.60572793164026,-0.06639955756851364&key=AsdKSk88xXVU3crLTQj1rIIlbMOX6GDhqw03rC2xkggIblqpcWx8JFdy0ojVcvaJ").json())
    distance=results['rows'][0]['elements'][0]['distance']['text']
    print(f"Appprox. Shipping Distance: {distance}")
    numericalDistance=distance.split()
    shippingCost=((float(numericalDistance[0])*8))
    print(f"Shipping Cost: £{shippingCost}")
    return shippingCost