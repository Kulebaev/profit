from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from oauth2client.service_account import ServiceAccountCredentials

def index_view(request):

    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)  # Разбиваем на 5 элементов на страницу
    page = request.GET.get('page')  # Получаем номер страницы из параметра GET

    products = paginator.get_page(page)  # Получаем объекты для текущей страницы

    return render(request, 'index.html', {'products': products})
    

def about_view(request):

    return render(request, 'index.html')


def reviews_view(request):

    return render(request, 'index.html')
