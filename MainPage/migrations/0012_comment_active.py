# Generated by Django 3.0.5 on 2020-05-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
