# Generated by Django 4.2 on 2023-05-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webMercArticles', '0010_alter_article_photoarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photoArticle',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]