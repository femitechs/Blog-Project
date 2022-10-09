from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Category, Comment


class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'post']


class CommentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'body']

        
class PostSerializer(serializers.ModelSerializer):    
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'publish', 'author', 'image', 'text', 'comments']


class CategorySerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['name', 'post']


# Based on Category list API, title field will only be needed
class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title']


# Based on Category list API, reference CategoryListSerializer to return post titles based on each category
class CategoryListPostSerializer(serializers.ModelSerializer):
    post = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name','post']






    