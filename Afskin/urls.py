from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product_list'),  # Mengubah categories menjadi products
    path('blog/', views.blog, name='blog'),
    path('pages/', views.page_list, name='page'),
    path('post/<slug:slug>/', views.post_detail, name='post'),
    path('page/<slug:slug>/', views.page_detail, name='page'),
]
