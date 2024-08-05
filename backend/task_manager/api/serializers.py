from rest_framework import serializers

from .models import Advert, Category, City, Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created', 'updated')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = ['id', 'created', 'title', 'description',
                  'city', 'category', 'views']
