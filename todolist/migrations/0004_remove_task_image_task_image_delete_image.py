# Generated by Django 4.0.6 on 2022-07-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_image_remove_task_image_task_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(null=True, upload_to='todolist/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
