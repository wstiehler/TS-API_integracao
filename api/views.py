from django.shortcuts import redirect, render
from api.form import VendasForm
from api.models import Vendas
import requests


def home(request):
    return render(request, 'home.html')


def product_post(request):
    url = 'http://192.168.16.3/product/'
    product_data_post = [{
    "name": "produto3",
    "description": "teste3",
    "price": 1000.0,
    "category": 3
    }]
    response = requests.post(url)
    product = response.json(product_data_post)
    return render(request, "home.html", {"product":product})

def product_get(request):
    url = requests.get('http://192.168.16.3/product/')
    product = url.json()
    return render(request, "home.html", {"product":product})


def list_all(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas_list_all.html', {'vendas':vendas})


def create(request):
    form = VendasForm(request.POST or None)
    url = requests.get('http://192.168.16.3/product/')
    product = url.json()


    if form.is_valid():
        form.save()
        return redirect('list_all_vendas')


    return render(request, 'vendas_form.html', {'form':form})


    


