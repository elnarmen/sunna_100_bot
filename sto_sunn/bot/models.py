from django.db import models
from markdownx.models import MarkdownxField


class Post(models.Model):
    text = MarkdownxField()
    image = models.ImageField("Изображение")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
