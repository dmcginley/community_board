# Generated by Django 5.1.6 on 2025-02-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_alter_navbarsettings_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarsettings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='navbar/'),
        ),
    ]
