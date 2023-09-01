from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Логин')
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput, label='Пароль')
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=100, required=True, label='Имя')
    company_name = forms.CharField(max_length=100, required=True, label='Наименование компании')
    phone_number = forms.CharField(max_length=20, required=True, label='Номер телефона')
