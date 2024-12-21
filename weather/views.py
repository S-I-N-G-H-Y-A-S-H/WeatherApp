from django.shortcuts import render
from .forms import CityForm
import requests

def index(request):
    form = CityForm()
    weather_data = None
    if request.method=='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8ef3d7f5406f8fb65c85fbbe6e586ea7&units=metric'
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                'city':data['name'],
                'temprature':data['main']['temp'],
                'description':data['weather'][0]['description'],
                }
            else:
                weather_data ={
                    'city':city,
                    'temprature':'N/A',
                    'description':'City not found!',
                }
    return render(request,'weather/index.html',{'form':form,'weather_data':weather_data})
