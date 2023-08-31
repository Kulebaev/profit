from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index_view(request):

    return render(request, 'index.html')


def login_view(request):

    if request.method != 'POST':
        return render(request, 'login.html')
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Проверяем введенные логин и пароль на соответствие существующему пользователю
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Если пользователь найден, выполняем вход
        login(request, user)
        return redirect('/')
    else:
        # Если пользователь не найден, выводим сообщение об ошибке
        error_message = "Неправильный логин или пароль."
        return render(request, 'login.html', {'error_message': error_message})
    

def logout_view(request):
    logout(request)
    return redirect('/login')  # Replace 'login' with the URL name of your login page


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        # Создаем нового пользователя
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        # Вместо простого перенаправления на страницу профиля,
        # можно добавить дополнительные действия, например, отправку
        # email с подтверждением регистрации или автоматический вход
        # пользователя после успешной регистрации.

        return redirect('/')  # Замените 'profile' на URL вашей страницы профиля пользователя

    return render(request, 'register.html')
    