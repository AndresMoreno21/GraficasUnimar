# Generated by Django 2.1.3 on 2018-11-22 23:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GraficasApp', '0007_auto_20181119_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='ingles',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(100)]),
        ),
    ]
