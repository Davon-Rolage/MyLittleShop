# Generated by Django 4.2.4 on 2023-08-09 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerstorage',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 18, 19, 47, 598365)),
        ),
    ]
