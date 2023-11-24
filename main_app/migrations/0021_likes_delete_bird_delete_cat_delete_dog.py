# Generated by Django 4.2.7 on 2023-11-23 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_follows_delete_bird_delete_cat_delete_dog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.posts')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        )
    ]
