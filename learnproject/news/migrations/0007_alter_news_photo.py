# Generated by Django 4.0.6 on 2022-08-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_news_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
