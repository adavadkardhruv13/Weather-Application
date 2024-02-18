from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ffd56210b11e0347fc77bcd548dd3cab').read()
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate": 'Longitude = '+ str(json_data['coord']['lon'])+' & Latitude = '+str(json_data['coord']['lat']),
            "temp": round(json_data['main']['temp']- 273.15),
            "feels_like": round(json_data['main']['feels_like'] - 273.15),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "clouds": str(json_data['clouds']['all'])+'%',
            "id": str(json_data['id']),
            "time": str(json_data['timezone']),


        }
    else :
        data = {}
        city = ''
    return render(request,'index.html', {'city':city, 'data': data})
