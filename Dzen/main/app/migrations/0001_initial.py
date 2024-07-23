# Generated by Django 5.0.7 on 2024-07-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('telegram_chat_id', models.CharField(max_length=50, verbose_name='Телеграмм')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
    ]
