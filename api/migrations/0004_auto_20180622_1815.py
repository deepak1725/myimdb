# Generated by Django 2.0.6 on 2018-06-22 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180621_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierecords',
            name='imdb_score',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='movierecords',
            name='popularity',
            field=models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
