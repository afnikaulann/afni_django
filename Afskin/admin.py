from django.contrib import admin
from .models import Product, Page, Blog  # Mengubah Category menjadi Product

class ProductAdmin(admin.ModelAdmin):  # Mengubah CategoryAdmin menjadi ProductAdmin
    list_display = ('product', 'slug')  # Mengubah category menjadi product
    prepopulated_fields = {'slug': ('product',)}  # Mengubah category menjadi product

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'product', 'status', 'created_date', 'published_date')  # Mengubah category menjadi product
    list_filter = ('product', 'status', 'created_date', 'published_date')  # Mengubah category menjadi product
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)  # Mengubah Category menjadi Product dan CategoryAdmin menjadi ProductAdmin
admin.site.register(Page, PageAdmin)
admin.site.register(Blog, BlogAdmin)
