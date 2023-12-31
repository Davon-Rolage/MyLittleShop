# Generated by Django 4.2.4 on 2023-08-09 21:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0013_alter_partner_added_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 1, 57, 27, 908944)),
        ),
        migrations.AlterField(
            model_name='partnerstorage',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 1, 57, 27, 908944)),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 1, 57, 27, 907943)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 1, 57, 27, 909945)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clothing.partnerstorage'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clothing.partner'),
        ),
    ]
