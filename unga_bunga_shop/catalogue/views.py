from django.shortcuts import render

from .models import Category

def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories_list.html', context)
