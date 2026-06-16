import requests
from datetime import datetime

CURRENT_LAT = 44.972923
CURRENT_LNG = -93.290142

#! API Parameters
#*      A way to give the API an input and receive a specific type of data back in return.
#*      Not all APIs have parameters.
# To see the Sunrise and Sunset API documentation: https://sunrise-sunset.org/api 

#? Creation of Parameters dictionary
#*      Parameters must match the parameters available in the API's documentation.

parameters = {
    "lat": CURRENT_LAT,
    "lng": CURRENT_LNG,
    "formatted": 0,
}

#? Add Parameters to GET request

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print("Raw", data)

#? Extracting Sunrise and Sunset data

sunrise_h = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunrise_m = data["results"]["sunrise"].split("T")[1].split(":")[1]
sunset_h = data["results"]["sunset"].split("T")[1].split(":")[0]
sunset_m = data["results"]["sunset"].split("T")[1].split(":")[1]

print("Sunrise is at: ",sunrise_h + ":" + sunrise_m, "UTC")
print("Sunset is at: ", sunset_h + ":" + sunset_m, "UTC")
print("UTC is 5 hours ahead of central time.")