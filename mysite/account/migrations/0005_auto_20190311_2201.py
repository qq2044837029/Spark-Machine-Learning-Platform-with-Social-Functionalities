# Generated by Django 2.0.5 on 2019-03-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190307_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default/default_profile.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
