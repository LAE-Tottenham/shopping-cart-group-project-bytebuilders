from geopy.geocoders import Nominatim
from haversine import haversine, Unit
import shop_functions, requests

#def get_coordinates(postcode):
    #geolocator = Nominatim(user_agent="geoapiExercises")
    #location = geolocator.geocode(postcode)
    #return (location.latitude, location.longitude)

#def calculate_distance(postcode1, postcode2):
    #coords_1 = get_coordinates(postcode1) #try use long and lat for place 1
    #coords_2 = get_coordinates(postcode2) #try use long and lat for place 2
    #distance = haversine(coords_1, coords_2, unit=Unit.KILOMETERS)
    #return distance

#Hardcoded place
#hardcoded_postcode = "N17 0BX"  # Example: Buckingham Palace, London

# Input postcode
#input_postcode = "N97 PR"  # Example: Spitalfields Market, London#

area, longitude, latitude, destination=shop_functions.postcodeValidation()

# Calculate distance
#distance = calculate_distance(hardcoded_postcode, input_postcode)
#print(f"The distance between N17 0BX and W10 4RE is {distance:.2f} km.")

#API Key AsdKSk88xXVU3crLTQj1rIIlbMOX6GDhqw03rC2xkggIblqpcWx8JFdy0ojVcvaJ

results=(requests.get(f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={latitude},{longitude}&destinations=51.60572793164026,-0.06639955756851364&key=AsdKSk88xXVU3crLTQj1rIIlbMOX6GDhqw03rC2xkggIblqpcWx8JFdy0ojVcvaJ").json())
distance=results['rows'][0]['elements'][0]['distance']['text']
print(distance)

#51.60572793164026, -0.06639955756851364