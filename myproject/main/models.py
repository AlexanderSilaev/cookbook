from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


# class CategoryWords(models.Model): # todo Добавить список ключевых слов для категорий
#     pass


class Achievement(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    short_text = models.TextField()
    is_done = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    achieved_date = models.DateTimeField()

    def __str__(self):
        return str(self.name)
