# Generated by Django 5.1.4 on 2025-01-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/'),
        ),
    ]
