# Generated by Django 5.1.6 on 2025-02-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_board_app', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
