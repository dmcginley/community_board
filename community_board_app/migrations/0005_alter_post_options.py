# Generated by Django 5.1.6 on 2025-02-20 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_board_app', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'posts'},
        ),
    ]
