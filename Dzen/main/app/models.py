from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    telegram_chat_id = models.CharField('Телеграмм', max_length=50)
    email = models.CharField('Почта', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    text = models.TextField('Текст поста')
    date = models.DateTimeField('Дата публикации')
    author = models.IntegerField('Автор')

    def __str__(self):
        return f"{self.author} - {self.text[:20]}"


class Comment(models.Model):
    post = models.IntegerField('Номер поста')
    author = models.IntegerField('Автор')
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f"{self.author} - {self.text[:20]}"

class Mark(models.Model):
    post = models.IntegerField('Номер поста')
    author = models.IntegerField('Автор')
    mark = models.IntegerField('Оценка', validators = [MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return f"{self.post} - {self.mark}"