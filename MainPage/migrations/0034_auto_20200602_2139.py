# Generated by Django 3.0.5 on 2020-06-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0033_auto_20200602_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='card1.jpg', null=True, upload_to=''),
        ),
    ]
