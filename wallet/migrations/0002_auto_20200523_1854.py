# Generated by Django 3.0.3 on 2020-05-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='income',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
