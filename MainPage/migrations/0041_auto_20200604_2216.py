# Generated by Django 3.0.5 on 2020-06-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0040_auto_20200604_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
