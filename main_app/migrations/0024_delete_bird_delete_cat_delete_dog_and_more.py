# Generated by Django 4.2.7 on 2023-11-23 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_delete_bird_delete_cat_delete_dog_remove_likes_feed_and_more'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='likes',
            name='profile',
        ),
    ]
