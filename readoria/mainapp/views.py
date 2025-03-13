from django.shortcuts import render

from .models import Book

# Create your views here.
from django.template import loader
from django.http import HttpResponse

def homeView(request):
    
    books = Book.objects.all()
    context = {
        'product_list' : books,
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))
