#from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    
    categories = Categories.objects.all()

    context: dict[str, str] = {
      'title': 'Сумеречная - Главная',
      'content': 'Магазин фэнтези и фантастики',
      'categories': categories

}

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict[str, str] = {
      'title': 'Сумеречная - О нас',
      'content': 'О нас',
      'text_on_page': 'Добро пожаловать в магазин фэнтези и фантастики. Этот магазин содержит только проверенные фэнтези проекты!))'
    }

    return render(request, 'main/about.html', context)
