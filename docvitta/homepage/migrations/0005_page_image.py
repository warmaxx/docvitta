# Generated by Django 5.0.1 on 2024-01-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/pages/', verbose_name='Изображение'),
        ),
    ]