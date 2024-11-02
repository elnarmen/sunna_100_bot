from django.db import models


class Post(models.Model):
    text = models.TextField("Текст")
    image = models.ImageField()

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
