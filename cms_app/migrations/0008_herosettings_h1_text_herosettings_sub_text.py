# Generated by Django 5.1.6 on 2025-02-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0007_herosettings_bg_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosettings',
            name='h1_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='herosettings',
            name='sub_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
