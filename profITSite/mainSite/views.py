from django.shortcuts import render
import gspread
import requests
import os
from oauth2client.service_account import ServiceAccountCredentials

def index_view(request):

    # data_from_sheets = get_google_sheets_data(spreadsheet_url, api_key, range_name)
    # Передайте данные в контекст шаблона
    context = {
        'data_from_sheets': "",
    }

    return render(request, 'index.html', context)
    

def about_view(request):

    return render(request, 'index.html')


def reviews_view(request):

    return render(request, 'index.html')
