#%%
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

api_keys = "84263b682936b3cec3c1881184dd334e"
# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count
print(len(cities))


## -- Personal Code -- ##
# Basic URL to interact with OpenWeatherMap's API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Basic settings for the data pull - Similar to work done in Ins_OpenWeatherWrapper
settings = {"units": "imperial", "appid": api_key}

# Summary list of required data. Looked at a single API pull for the setup of the returned json data:
#(http://api.openweathermap.org/data/2.5/weather?appid={apikey}&q=city&units=imperial). 
# Similar to work done in Ins_OpenWeatherWrapper but using **kwargs insteead of *args
data_list = ['name', 'clouds.all', 'sys.country', 'dt', 'main.humidity', 'coord.lon', 'coord.lat', 'main.temp_max', 'wind.speed']

# testing current setup
# test_data = owm.get_current("la jolla", **settings) 
# summary_test = test_data(*summary)
# pprint(summary_test)
# ('La Jolla', 1, 'US', 1567465761, 65, -117.27, 32.85, 93.2, 4.7)

# Empty lists to store the pulled data
lng = []
lat = []
date = []
temp = []
country = []
city_list = []
humidity  = []
wind_speed = []
cloudiness = []

# Setting initial states for the counters. It appears from the original code ipynb that the returned data needs to be broken up into Sets after getting 50 or so results. 
city_count = 1
set_count = 1

#%%
