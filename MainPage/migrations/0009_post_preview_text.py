# Generated by Django 3.0.5 on 2020-04-25 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_auto_20200425_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
