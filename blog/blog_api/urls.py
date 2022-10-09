from django.urls import path
from .views import PostDetails, PostList, CommentList, CategoryList


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
    path('comments/', CommentList.as_view()),
    path('<slug:slug>/', CategoryList.as_view()),
]
