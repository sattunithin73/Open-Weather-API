from django.shortcuts import render
import requests
# Create your views here.
api_key = 'bbb94c04c086d2f8c090b7da23efdb62'
def home(request):
    print(request.method) #GET #GET
    print(request.GET) #QueryDict: {'city': ['Hyderabad']}
    if 'city' in request.GET:
        city_name = request.GET['city']
        print(city_name) #Hyderabad
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
        py_data = resp.json()
        print(py_data)
        return render(request,'home.html',{'data':py_data})
    return render(request,'home.html')