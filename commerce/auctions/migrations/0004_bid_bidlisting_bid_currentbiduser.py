# Generated by Django 4.1.5 on 2023-02-17 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_user_listing_user_comment_commenttext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidListing',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='bid',
            name='currentBidUser',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]