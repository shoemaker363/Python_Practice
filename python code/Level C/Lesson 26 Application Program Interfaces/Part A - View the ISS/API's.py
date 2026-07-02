
#! Application Program Interfcace (API)
#*     An API is a set if commands, functions, protocols and objects that programmers can use to
#*          create software or interact with an external system.

#? One of the most important aspects of an API is an API Endpoint.
#*     Usually just a URL where the API data can be pulled from.

#? API Request
#* Program is asking for data from the API Endpoint.
# To see the User Guide for requests module: https://docs.python-requests.org/en/latest/

#? APIs need the libraray requests imported

import requests

#? Using requests library method called 'get' to pull the API data.
#*      url is the address from which the API data is at.

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
#@                  Receiving a response code:
#*                              - 1XX: Request received and the server is processing.
#*                              - 2XX: HTTP request was succesfully received, understood, and accepted by the server.
#*                              - 3XX: Signals that the endpoint needs to be changed by the client.
#*                              - 4XX: Indicates client-side error / An issue with clients's input or permissions.
#*                              - 5XX: Indicates server-side error.
#                               To see more Status Codes and Terms: https://www.webfx.com/web-development/glossary/

#? Extracting the JSON data from the API

data = response.json()
print("Raw Data", data)

#? Managing the JSON data in a dictionary

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_postition = (longitude, latitude)

print("Managed Data", iss_postition)