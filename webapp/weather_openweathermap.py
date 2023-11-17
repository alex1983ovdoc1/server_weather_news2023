from flask import current_app
import requests

print

def weather_by_city(city_name):
	lat=37.983810
	lon=23.727539
	params1 = {
		'lat': 37.983810,
		'lon':23.727539,
		'units': 'metric',
		# 'appid': current_app.config['WEATHER_API_KEY']
		'appid': '05966ac74347d94fb6dcd48d722b66eb'
	}
	# weather_url = current_app.config['WEATHER_URL']
	weather_url = 'https://api.openweathermap.org/data/2.5/weather?'
	try:
		result = requests.get(weather_url, params=params1)
		# result = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=37.983810&lon=23.727539&units=metric&appid=05966ac74347d94fb6dcd48d722b66eb')
		weather = result.json()
		print(weather)
		if "main" in weather:
			if "temp" in weather["main"]:
				try:
					return weather["main"]["feels_like"]
				except(IndexError, TypeError):
					return False
	except(ValueError): # Network Error
		print("--/Newwork Error/ --")
		return False

	return False


if __name__=='__main__':
	w = weather_by_city('Kyiv,Ukraine')
	print(w)