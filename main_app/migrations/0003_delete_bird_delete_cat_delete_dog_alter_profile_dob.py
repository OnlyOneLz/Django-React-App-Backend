# Generated by Django 4.2.7 on 2023-11-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feed_media_posts_profile_delete_bird_delete_cat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.IntegerField(),
        ),
    ]