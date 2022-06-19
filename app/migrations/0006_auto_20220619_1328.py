# Generated by Django 3.1.2 on 2022-06-19 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_logo',
            field=models.ImageField(blank='true', default='', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank='true', default='default.jpg', upload_to='media/profile/'),
        ),
    ]
