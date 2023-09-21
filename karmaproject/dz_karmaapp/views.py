from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage

from .forms import ClientForm, ProductForm
from .models import Client, Product, Order
from django.http import HttpResponse
import logging
from datetime import date, timedelta

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Main page accessed')
    html = """
        My name is Karma."""
    return HttpResponse(f'<h1>{html}</h1>') 

def about(request):
    html = """
        This is my first <b>Django-site</b>.<br>
        <i>And I hope, not the last one.</i> :)
        """
    logger.debug('About page accessed')
    return HttpResponse(html) 

def client_orders_7days(request, client_id): # допилить
    startdate = date.today()
    enddate = startdate + timedelta(days=6)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).filter(date__range=[startdate, enddate]).order_by('date_ordered') # ???
    return render(request, 'myapp3/client_orders.html', {'client': client, 'orders':orders})

def client_form(request):
    if request.method =='POST':
        form = ClientForm(request.POST)
        message='Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            address = form.cleaned_data['address']
            logger.info(f'Client: {name=}, {email=}, {tel=}, {address=}')
            client = Client(name=name, email=email, tel=tel, address=address)
            client.save()
            message='Пользователь сохранён'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'dz_karmaapp/client_form.html', {'form': form, 'message': message})

def product_form(request):
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        message='Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            foto = form.cleaned_data['foto']
            product = Product(name=name, description=description, price=price, foto=foto)
            fs = FileSystemStorage()
            fs.save(foto.name, foto)
            logger.info(f'Got: {form.cleaned_data=}')
            message='Продукт сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'dz_karmaapp/product_form.html', {'form': form, 'message': message})
