from django.shortcuts import render, redirect
import requests

# Create your views here.


def index(request):

    data_list = {}
    if request.method == "POST":
        
        try:
            # post based on the city
            city = request.POST['city']
            api_url = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' +
                                city + '&units=imperial&appid=aa237aa0b8bfefa9b4156b04460b1e24')

            data_list = api_url.json()
        except:
            return redirect('index')

    return render(request, 'app/index.html', {'data_list':data_list})

def about(request):
    
    return render(request, 'app/about.html')