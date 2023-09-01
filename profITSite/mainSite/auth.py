from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm


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
    form = RegistrationForm()

    if request.method != 'POST':
        return render(request, 'register.html', {'form': form})
    
    if not form.is_valid():
        return render(request, 'register.html', {'form': form})
    
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    email = form.cleaned_data['email']
    first_name = form.cleaned_data['first_name']
    company_name = form.cleaned_data['company_name']
    phone_number = form.cleaned_data['phone_number']

    # Создаем нового пользователя
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
    )
    user.userprofile.company_name = company_name
    user.userprofile.phone_number = phone_number
    user.userprofile.save()

    # Вместо простого перенаправления на страницу профиля,
    # можно добавить дополнительные действия, например, отправку
    # email с подтверждением регистрации или автоматический вход
    # пользователя после успешной регистрации.

    return redirect('/')

    
    