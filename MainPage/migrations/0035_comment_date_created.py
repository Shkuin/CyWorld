# Generated by Django 3.0.5 on 2020-06-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0034_auto_20200602_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]