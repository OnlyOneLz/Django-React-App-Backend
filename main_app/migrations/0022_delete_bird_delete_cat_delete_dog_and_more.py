# Generated by Django 4.2.7 on 2023-11-23 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_likes_delete_bird_delete_cat_delete_dog'),
    ]

    operations = [

        migrations.RenameField(
            model_name='likes',
            old_name='Posts',
            new_name='Feed',
        ),
    ]
