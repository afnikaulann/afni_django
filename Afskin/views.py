# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Blog, Page

def home(request):
    return render(request, 'home.html')

def product(request):
    products = Product.objects.all()  # Mengubah categories menjadi products
    return render(request, 'product.html', {'products': products})

def blog(request):
    blogs = Blog.objects.filter(status=1).order_by('-published_date')
    return render(request, 'blog.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html', {'about': about})

def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def article3(request):
    return render(request, 'article3.html')

def article4(request):
    return render(request, 'article4.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def contact(request):
    return render(request, 'contact.html', {'contact': contact})

