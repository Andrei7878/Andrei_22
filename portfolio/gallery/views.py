from .models import Category, Gallery
from django.shortcuts import render


def gallery_index(request):
    gallery = Gallery.objects.all().order_by('-created_on')
    context = {
        'gallery': gallery
    }
    return render(request, 'gallery_index.html', context)

def gallery_category(request, category):
    gallery = Gallery.objects.filter(categries__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'gallery': gallery
    }
    return render(request, 'gallery_category.html', context)

def gallery_detail(request, pk):
    gallery = Gallery.objects.get(pk=pk)
    context = {
        'gallery': gallery
    }
    return render(request, 'gallery_detail.html', context)
