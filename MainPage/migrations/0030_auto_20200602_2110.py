# Generated by Django 3.0.5 on 2020-06-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0029_auto_20200522_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='card1.jpg', null=True, upload_to=''),
        ),
    ]