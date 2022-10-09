from unicodedata import category
from rest_framework import generics
from blog.models import Post, Category, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, CategoryListPostSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class PostDetails(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentList(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListPostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Category.objects.filter(slug=slug)