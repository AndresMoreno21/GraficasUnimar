# Generated by Django 2.1.3 on 2018-11-27 04:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GraficasApp', '0014_auto_20181126_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='inglesp',
            field=models.IntegerField(blank=0, default=1, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
