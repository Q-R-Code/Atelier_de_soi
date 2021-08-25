from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import BlogPost


class TestViews(TestCase):
    """Test some views"""

    def setUp(self):
        """setUP USer instance and article for blog"""
        User.objects.create(
            username="user1", email="user1@user1.com", password="azerty"
        ).save()
        self.user1 = User.objects.get(username="user1")
        BlogPost.objects.create(
            title="Article test 1",
            slug="article-test-1",
            author=self.user1,
            published=True,
            content="Article test 1 Article test 1 Article test 1"
        ).save()

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_list.html')

    def test_article_view(self):
        response = self.client.get(str("/blog/article-test-1/"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_detail.html')
