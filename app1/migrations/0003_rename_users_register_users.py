# Generated by Django 4.1.4 on 2022-12-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Register_users',
        ),
    ]
