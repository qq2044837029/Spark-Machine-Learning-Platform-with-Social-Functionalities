# Generated by Django 2.0.5 on 2019-03-07 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        # ('auth', '0011_remove_user_following'),
        ('account', '0003_auto_20190307_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_to',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
