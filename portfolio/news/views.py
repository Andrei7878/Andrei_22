from .models import Category, News
from django.shortcuts import render


def news_index(request):
    news = News.objects.all().order_by('-created_on')
    context = {
        'news': news
    }
    return render(request, 'news_index.html', context)

def news_category(request, category):
    news = News.objects.filter(categries__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'news': news
    }
    return render(request, 'news_category.html', context)

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)
