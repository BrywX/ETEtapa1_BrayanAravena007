# Generated by Django 3.2.4 on 2021-06-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn', '0003_colab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colab',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]
