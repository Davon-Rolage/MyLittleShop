# Generated by Django 4.2.4 on 2023-08-09 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0012_pricelist_added_at_alter_partner_added_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 20, 51, 11, 798978)),
        ),
        migrations.AlterField(
            model_name='partnerstorage',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 20, 51, 11, 798978)),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='added_at',
            field=models.DateTimeField(default='09.08.2023 20:51:11'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 20, 51, 11, 799937)),
        ),
    ]
