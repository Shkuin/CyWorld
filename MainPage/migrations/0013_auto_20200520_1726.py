# Generated by Django 3.0.5 on 2020-05-20 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0012_comment_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
    ]
