# Generated by Django 3.2.4 on 2021-07-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn', '0005_rename_region_colab_region'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pais',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.AlterField(
            model_name='colab',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='colab',
            name='pais',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='colab',
            name='region',
            field=models.CharField(max_length=20),
        ),
    ]
