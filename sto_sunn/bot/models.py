from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    text = HTMLField("Текст")
    image = models.ImageField("Изображение")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
