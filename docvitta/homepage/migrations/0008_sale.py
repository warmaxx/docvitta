# Generated by Django 5.0.1 on 2024-02-14 20:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sales/', verbose_name='Изображение')),
                ('file', models.FileField(blank=True, null=True, upload_to='images/sales/', verbose_name='Описание акции')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
        ),
    ]
