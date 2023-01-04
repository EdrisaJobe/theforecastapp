from django.shortcuts import render, redirect
import requests

# Create your views here.


def index(request):

    # if request.method == "POST":
        
    #     try:
    #         # post based on the city
    #         city = request.POST['city']
    #         api_url = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' +
    #                             city + '&units=metric&appid=aa237aa0b8bfefa9b4156b04460b1e24')

    #         data_list = api_url.json()
    #     except:
    #         return redirect('/')

    return render(request, 'app/index.html')
