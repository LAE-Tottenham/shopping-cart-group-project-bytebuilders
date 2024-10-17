import requests

items = {
    'Bread': 1.20,
    'Milk': 1.15,
    'Chocoloate': 0.5,
}

def start_shop():
    while True:
        print("What you would like to buy? ")
        # display items to buy

    # blah blah blah

    return {
        'items': [],
        'total_cost': 0
    }
        
        
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
    #MUST run 'area, longitude, latitude, destination=postcodeValidation()' in MAIN code to obtain necessary variables for distanceCalculation function

area, longitude, latitude, destination=postcodeValidation()

def distanceCalculation(longitude, latitude):
    results=(requests.get(f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={latitude},{longitude}&destinations=51.60572793164026,-0.06639955756851364&key=AsdKSk88xXVU3crLTQj1rIIlbMOX6GDhqw03rC2xkggIblqpcWx8JFdy0ojVcvaJ").json())
    distance=results['rows'][0]['elements'][0]['distance']['text']
    print(f"Appprox. Shipping Distance: {distance}")
    numericalDistance=distance.split()
    shippingCost=((float(numericalDistance[0])*8))
    print(f"Shipping Cost: £{shippingCost}")
    return shippingCost
    #MUST run shippingCost=distanceCalculation(longitude,latitude) in MAIN code to obtain necessary values (or any other variable name for the shipping cost))

