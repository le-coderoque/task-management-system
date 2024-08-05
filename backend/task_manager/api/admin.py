from django.contrib import admin
from .models import Advert, Category, City, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'updated', 'user')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'description',
                    'city', 'category', 'views')

