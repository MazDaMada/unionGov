# Generated by Django 3.2.5 on 2021-07-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configref',
            name='config_ref',
            field=models.CharField(default='qHTn1g3C9aE4HEgk3PbUHRvws555ccWW', max_length=32),
        ),
    ]