from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from oauth2client.service_account import ServiceAccountCredentials
from .bot import bot
from django.contrib import messages
from django.shortcuts import redirect


def index_view(request):

    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)  # Разбиваем на 5 элементов на страницу
    page = request.GET.get('page')  # Получаем номер страницы из параметра GET

    products = paginator.get_page(page)  # Получаем объекты для текущей страницы

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        comment = request.POST.get('comment')

        # Создайте текст сообщения для отправки
        message_text = f"Имя: {name}\nНомер: {number}\nКомментарий: {comment}"

        # Отправьте сообщение в Telegram
        chat_id = '-1001900918491'
        bot.send_message(chat_id ,message_text)
        
        messages.success(request, 'Сообщение успешно отправлено!')

        return redirect('index')  
        
    return render(request, 'index.html', {'products': products})

    
    

def about_view(request):

    return render(request, 'index.html')


def reviews_view(request):

    return render(request, 'index.html')
