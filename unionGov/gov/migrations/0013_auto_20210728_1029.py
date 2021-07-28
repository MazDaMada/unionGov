# Generated by Django 3.2.5 on 2021-07-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov', '0012_auto_20210728_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='configref',
            name='config_ref',
            field=models.CharField(default='EcezKPQVYuvLV3i4M3cjDrMboBLFPP3I', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(max_length=64),
        ),
    ]
