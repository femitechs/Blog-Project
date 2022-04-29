from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'publish', 'created')
    list_filter = ('created', 'publish', 'category')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_field = ('category')
    date_hierarchy = 'publish'
    ordering = ('publish',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
