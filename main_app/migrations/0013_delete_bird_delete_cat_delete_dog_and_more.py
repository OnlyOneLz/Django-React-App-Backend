# Generated by Django 4.2.7 on 2023-11-20 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_delete_bird_delete_cat_delete_dog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
