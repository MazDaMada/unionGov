# Generated by Django 3.2.6 on 2021-09-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov', '0013_auto_20210728_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configref',
            name='config_ref',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(max_length=128),
        ),
    ]