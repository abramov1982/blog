from abc import ABC

from blog.apps.app.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    category = PostCategorySerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    post = PostSerializer(required=False, many=True)

    class Meta:
        model = Category
        fields = ['cat_name', 'post']
