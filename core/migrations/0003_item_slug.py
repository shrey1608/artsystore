# Generated by Django 3.0.6 on 2020-05-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200528_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]
