from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('details/<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.post_details, name='details'),
    path('category/<slug:category_target>/', views.category_list, name='category_list'),
    #path('general/', views.all_post_list, name='general'),

]
