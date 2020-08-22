from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=20, verbose_name='Категория')

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return self.pk

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = 'app'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')], verbose_name='Статус')
    content = models.TextField(verbose_name='Содержание')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='category')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return self.pk

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        app_label = 'app'
