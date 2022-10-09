from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='123456')
        testuser1.save()
        testcategory = Category.objects.create(name='cat1')
        testcategory.save()
        testpost = Post.objects.create(author=testuser1, category=testcategory, title='Blog title', text='Full details ...')
        testpost.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        category = f'{post.category}'
        title = f'{post.title}'
        text = f'{post.text}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(category, 'cat1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(text, 'Full details ...')
