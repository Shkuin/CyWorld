# Generated by Django 3.0.5 on 2020-06-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0038_auto_20200604_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
