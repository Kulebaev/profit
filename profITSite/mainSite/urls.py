from django.urls import path
from . import auth, views, testJSON


urlpatterns = [
    path('', views.index_view, name='index'),
    path('process_json_full_clear/', testJSON.process_json_full_clear, name='process_json_full_clear'),
    path('process_json/', testJSON.process_json, name='process_json'),
    # path('reviews/', views.reviews_view, name='reviews'),
    # path('login/', auth.login_view, name='login'),
    # path('login/', auth.login_view, name='login'),
    # path('logout/', auth.logout_view, name='logout'),
    # path('register/', auth.register_view, name='register')
]