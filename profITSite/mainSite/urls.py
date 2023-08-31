from django.urls import path
from . import auth


urlpatterns = [
    path('', auth.index_view, name='index'),
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('register/', auth.register_view, name='register')
]