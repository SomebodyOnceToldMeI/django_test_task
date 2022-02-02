# Generated by Django 4.0.1 on 2022-02-02 14:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date set'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'liker')},
        ),
    ]
