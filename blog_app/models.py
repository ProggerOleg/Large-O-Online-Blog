from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField(max_length=20)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_url': self.url})

    class Meta:
        verbose_name = 'Список постов'
        verbose_name_plural = 'Список постов'
        ordering = ['-time_create', 'title']

#
# class Tag(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Теги')
#     slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="URL")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('tag', kwargs={'tag_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Тег'
#         verbose_name_plural = 'Теги'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)
        
