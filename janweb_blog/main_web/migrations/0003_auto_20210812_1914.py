# Generated by Django 3.2.5 on 2021-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0002_deletedarticles'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='changed_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='DeletedArticles',
        ),
    ]
