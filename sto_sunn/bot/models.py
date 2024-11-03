from django.db import models
from markdownx.models import MarkdownxField


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Interval(SingletonModel):
    hours = models.PositiveIntegerField("Часы")

    class Meta:
        verbose_name = "Интервал между постами"
        verbose_name_plural = "Интервал между постами"


class Post(models.Model):
    text = MarkdownxField("Текст")
    image = models.ImageField("Изображение")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
