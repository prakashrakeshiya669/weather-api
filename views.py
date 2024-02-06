from django.shortcuts import render
import requests
import json
import urllib.request

# Create your views here.
def userhome(request):
    city=request.GET.get('city', "seoni")
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=16b7ef72a78b6ad9782a508a4c3456ed'
    data = requests.get(url).json()
    #print(data)
    payload={
        'city' :data['name'], 
        'weather': data['weather'][0]['main'], 
        'icon' : data['weather'][0]['icon'], 
        'kelvin_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp'] -273)
,        'pressure' : data['main']['pressure'], 
        'humidity' :data['main']['humidity'],
        'feels_like' :data['main']['feels_like'],
        'description' : data['weather'][0]['description'],
    }

    context = {'data':payload}
    print(context)
    return render(request, 'userhome.html',context)