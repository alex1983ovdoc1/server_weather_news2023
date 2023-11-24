import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__)) # address



WEATHER_DEFAULT_CITY = 'Washington'											# weather location
LAT_CITY = 47.751076
LON_CITY = -120.740135

WEATHER_API_KEY = '05966ac74347d94fb6dcd48d722b66eb'		 # from https://openweathermap.org/
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?'

SECRET_KEY = "szdgdfhgfjghkfhgkeaf$wer"

REMEMBER_COOKIE_DURATION = timedelta(days=150) # remember users days=5

SQLALCHEMY_TRACK_MODIFICATIONS = False
																				# "sqlite:///" -> name DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db') # DB sqlite -> addres + name file.db "webapp.db"