from django.shortcuts import render
import requests

# Create your views here.


def index(request):

    if request.method == "POST":

        city = request.POST['city']
        api_url = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' +
                               city + '&units=metric&appid=aa237aa0b8bfefa9b4156b04460b1e24')

        data_list = api_url.json()

        data = {
            "icon": data_list["weather"][0]["icon"],
            "country_code": str(data_list["sys"]["country"]),
            "coordinate": str(data_list["coord"]["lon"]) + ", " + str(data_list["coord"]["lat"]),
            "temp": str(data_list["main"]["temp"]) + "°C",
            "pressure": str(data_list["main"]["pressure"]),
        }
        print(data)
    else:
        data = {}

    return render(request, 'app/index.html', data)
