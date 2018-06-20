from django.http import HttpResponse
from django.shortcuts import render
import requests

def homepage(request):
    return render(request, 'main.html')

def logopage(request):
    data = request.GET['brand']
    # url = "https://autocomplete.clearbit.com/v1/companies/suggest?query="+str(data)
    # json_data = requests.get(url)
    # image_url = json_data.json()[0]['logo']
    image_url = "https://logo.clearbit.com/"+str(data)+".com"
    return render(request, 'logo.html', {'image_url':image_url})
