# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Blog, Page

def home(request):
    return render(request, 'blog/home.html')

def product(request):
    products = Product.objects.all()  # Mengubah categories menjadi products
    return render(request, 'blog/product_list.html', {'products': products})

def blog(request):
    blogs = Blog.objects.filter(status=1).order_by('-published_date')
    return render(request, 'blog/blog.html', {'blogs': blogs})

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'blog/page_list.html', {'pages': pages})

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'blog/page_detail.html', {'page': page})
