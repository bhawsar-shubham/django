from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date
import time
def index(request):
    """url='http://api.openweathermap.org/data/2.5/weather?appid=870558c0cc3974b63884eb1d7311e0bb&q=Indore&units=metric
    #Your API key is 870558c0cc3974b63884eb1d7311e0bb
    city='Indore'

    r=requests.get(url.format(city)).json()
    #print(r.text)"""
    if request.method == 'POST': 
        city = request.POST['city']
        api_add='http://api.openweathermap.org/data/2.5/weather?appid=870558c0cc3974b63884eb1d7311e0bb&units=metric&q='
    #city='Indore'
        url=api_add+city
        json_data=requests.get(url).json()
    #print(json_data)
        city_weather={
             'city':city,
             'temprature':json_data['main']['temp'],
             'description':json_data['weather'][0]['description'],
             'humidity':json_data['main']['humidity'],
             'pressure':json_data['main']['pressure'],
             'wind':json_data['wind']['speed'],
             'icon':json_data['weather'][0]['icon'],
             'dt':time.asctime(time.localtime(time.time()))    
        }
        #print(city_weather)
        context={'city_weather':city_weather}
        return render(request,'weather/weather.html',context)

    else:
        context={}
        return render(request,'weather/weather.html',context)