import requests


weather_api = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"

'''
endpoint - weather 
2 parameters - q{city name} and appid{API key}
'''

city_name = 'Hyderabad'

api_key = "bbb94c04c086d2f8c090b7da23efdb62"

resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')

print(resp)#<Response [200]>

'''
<Response [200]> - request successful
<Response [404]> - city not found
<Response [401]> - invalid API key
<Response [500]> - server error 
<Response [400]> - bad request

json data will be in response body 
if we want to get python data from the json response body we have json()
'''

print(resp.json()) 
'''
{'coord': {'lon': 78.4744, 'lat': 17.3753}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 308.38, 'feels_like': 307.74, 'temp_min': 308.38, 'temp_max': 308.88, 'pressure': 1005, 'humidity': 28, 'sea_level': 1005, 'grnd_level': 943}, 'visibility': 5000, 'wind': {'speed': 4.63, 'deg': 40}, 'clouds': {'all': 40}, 'dt': 1776771841, 'sys': {'type': 1, 'id': 9214, 'country': 'IN', 'sunrise': 1776731171, 'sunset': 1776776591}, 'timezone': 19800, 'id': 1269843, 'name': 'Hyderabad', 'cod': 200}
'''
print(type(resp.json()))#<class 'dict'>