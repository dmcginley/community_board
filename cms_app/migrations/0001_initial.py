# Generated by Django 5.1.6 on 2025-02-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='My Site', max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='navbar/')),
            ],
            options={
                'verbose_name_plural': 'Navbar Settings',
            },
        ),
    ]
