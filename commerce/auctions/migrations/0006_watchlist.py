# Generated by Django 4.1.5 on 2023-02-18 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_user_listing_creator_remove_listing_startbid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listingID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('userID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]