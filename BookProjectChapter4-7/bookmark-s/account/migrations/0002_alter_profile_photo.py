# Generated by Django 4.2.3 on 2023-07-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.jpg', upload_to='users/%Y/%m/%d/'),
        ),
    ]
