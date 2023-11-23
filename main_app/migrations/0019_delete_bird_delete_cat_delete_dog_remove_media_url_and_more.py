# Generated by Django 4.2.7 on 2023-11-21 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_delete_bird_delete_cat_delete_dog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='url',
        ),
        migrations.AddField(
            model_name='media',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='document',
            field=models.FileField(default=1, max_length=30, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]