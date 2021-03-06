"""Tables for the database
BlogPost for the articles
Comment for the comments under each articles

"""

from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Allows you to create a slug automatically if it is not notified"""
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blog_home")

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Auteur')
    content = models.TextField(blank=True, verbose_name="Contenu")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Publié")

    class Meta:
        ordering = ['created_on']
        verbose_name = "Commentaires"

    def __str__(self):
        return 'Commenté {} par {}'.format(self.content, self.author)
