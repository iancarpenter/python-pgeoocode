# Generated by Django 3.2.7 on 2021-09-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcode',
            name='end_postcode',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='start_postcode',
            field=models.CharField(max_length=4),
        ),
    ]
