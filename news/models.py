from django.db import models

# Вывод новости
class Post(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:124]}'


# Категория, к которой будет привязываться новость
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name.title()
