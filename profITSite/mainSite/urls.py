from django.urls import path
from . import auth, views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('reviews/', views.reviews_view, name='reviews'),
    # path('login/', auth.login_view, name='login'),
    # path('login/', auth.login_view, name='login'),
    # path('logout/', auth.logout_view, name='logout'),
    # path('register/', auth.register_view, name='register')
]