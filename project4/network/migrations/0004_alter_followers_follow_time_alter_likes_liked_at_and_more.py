# Generated by Django 4.2.1 on 2023-05-16 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_followers_follow_time_alter_likes_liked_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follow_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 10, 43, 19, 991977)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='liked_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 10, 43, 19, 991977)),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 10, 43, 19, 990978)),
        ),
    ]