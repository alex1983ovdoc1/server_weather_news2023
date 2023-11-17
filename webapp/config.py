import os
from datetime import timedelta
# print(os.path.abspath(os.path.dirname(__file__)))
basedir = os.path.abspath(os.path.dirname(__file__)) # address
# print(os.path.join(basedir, '..', 'webapp.db'))


WEATHER_DEFAULT_CITY = 'Kyiv,Ukraine'											# weather location
# WEATHER_API_KEY = '38d7d237f2eb4546975144035232704'								# key weather
# WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?'		# url weather

# https://api.openweathermap.org/data/2.5/weather?lat=37.983810&lon=23.727539&units=metric&appid=05966ac74347d94fb6dcd48d722b66eb
WEATHER_API_KEY = '05966ac74347d94fb6dcd48d722b66eb'		 # from https://openweathermap.org/
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?'

SECRET_KEY = "szdgdfhgfjghkfhgkeaf$wer"

REMEMBER_COOKIE_DURATION = timedelta(days=5) # remember users days=5

SQLALCHEMY_TRACK_MODIFICATIONS = False
																				# "sqlite:///" -> name DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db') # DB sqlite -> addres + name file.db "webapp.db"