from django.contrib import admin
from students.models import Category, Students, Products
# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Products)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk',)
    search_fields = ('name', 'description',)
