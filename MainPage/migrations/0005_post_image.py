# Generated by Django 3.0.5 on 2020-04-21 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0004_post_preview_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/img'),
            preserve_default=False,
        ),
    ]