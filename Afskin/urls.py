from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product_list'),  # Mengubah categories menjadi products
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('blog/article1/', views.article1, name='article1'),
    path('blog/article2/', views.article2, name='article2'),
    path('blog/article3/', views.article3, name='article3'),
    path('blog/article4/', views.article4, name='article4'),
    path('pages/', views.page_list, name='pages'),
    path('post/<slug:slug>/', views.post_detail, name='post'),
    path('page/<slug:slug>/', views.page_detail, name='page'),
]
