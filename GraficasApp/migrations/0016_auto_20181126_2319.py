# Generated by Django 2.1.3 on 2018-11-27 04:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GraficasApp', '0015_auto_20181126_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='inglesp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(0)]),
        ),
    ]
