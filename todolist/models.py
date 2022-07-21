from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task (models.Model):
    status_choices = (
        ('NEW', 'New'),
        ('INPROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
    )

    title = models.CharField(
        verbose_name='Название задачи',
        max_length=100,
    )
    text = models.TextField(
        verbose_name='Описание задачи'
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор',
    )
    worker = models.ManyToManyField(
        User,
        related_name='worker',
        blank=True,
        )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    edit_date = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(blank=True)