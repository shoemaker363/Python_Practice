
#! API Authentication
#*  - Used to access more Secure and Useful data from an API Provider.
#*  - API Key: Used to track users account and monitor usage data.

#! Weather API
#   To get your own API key, go to: https://openweathermap.org/


#? 5 Day weather forecast
# import requests

# five_day_forecast = "https://api.openweathermap.org/data/2.5/forecast"  ## Endpoint for 5 day weather forecast API

# five_day_key = "API Key"       ## API Key input as a variable
#                                                         #*  Input your own API Key.
# five_params = {
#     "lat": 44.9772995,          ## Latitude
#     "lon": -93.2654692,         ## Longitude
#     "appid": five_day_key,      ## API Key
#     "units": "imperial",        ## Units of measurment
# }

# response = requests.get(five_day_forecast, params=five_params)     ## Calling the API with the parameters included.
# print(response.status_code)                                        ## Should result in a code of 200. 
# response.raise_for_status()                                        ## If code is not 200, provides an exception. 
# print(response.json())                                             ## Prints all the data requested in JSON format. 


#? Next 12 hour check for rain. 
import requests

five_day_forecast = "https://api.openweathermap.org/data/2.5/forecast"  ## Endpoint for 5 day weather forecast API
five_day_key = "API Key"       ## API Key input as a variable
                                                        #*  Input your own API Key.
five_params = {
    "lat": 44.9772995,          ## Latitude
    "lon": -93.2654692,         ## Longitude
    "appid": five_day_key,      ## API Key
    "units": "imperial",        ## Units of measurment
    "cnt": 4,                   ## Number of timestamps returned
}

response = requests.get(five_day_forecast, params=five_params)     ## Calling the API with the parameters included. 
response.raise_for_status()                                        ## If code is not 200, provides an exception. 
weather_data = response.json()                                     ## Retrieves data requested in JSON format. 
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:                             ## Pulling weather data for next 12 hours 
    condition_code = hour_data["weather"][0]["id"]                 ## Extracting the API condition codes for weather 
    if int(condition_code) < 700:                                  ## Checking if code meets criteria for rain/snow 
        will_rain = True
if will_rain:                                                      ## If it is supposed to rain in the next 12 hours 
    print("Bring an umbrella")