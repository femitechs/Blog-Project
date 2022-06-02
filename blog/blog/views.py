
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from blog.forms import CommentForm
from .models import Post, Category
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_list(request):
    
    post = {category: 
        Post.objects.filter(category = category).order_by('-publish')[:5] for category in Category.objects.all()}
    
    context = {'post':post}
    return render(request, 'blog/list.html', context)


def post_details(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug, 
                                      publish__year=year, 
                                      publish__month=month, 
                                      publish__day=day)

    #This will retrieve similar post for a specific post
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:2]

    #List active comments,then instatiate and process the comment form
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()
    return render(request, 'blog/details.html', 
            {'post': post, 'form':form, 'comments':comments, 'new_comment':new_comment, 'similar_posts':similar_posts})   


def category_list(request, category_target):
    
    category_post = Post.objects.filter(category__slug=category_target)
    page = request.GET.get('page', 1)
    paginator = Paginator(category_post, 2)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html', {'numbers': numbers, 'category_target':category_target.title()})
    





