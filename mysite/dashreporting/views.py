from django.shortcuts import render
from . import dash_apps
from . import django_plotly_dash


def dash1(request):
    print("Burası Çalıştı")
    return render(request, 'dash.html')
