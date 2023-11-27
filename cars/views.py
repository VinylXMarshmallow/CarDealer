# cars/views.py
from django.shortcuts import render
from .models import Car
from .models import Article
from django.http import HttpResponse


def car_list(request):
    articles = Article.objects.all()
    return render(request, 'cars/car_list.html', {'articles': articles})

def test_response(request):
    return HttpResponse("To jest przykładowy url")



