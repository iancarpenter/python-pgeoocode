# Generated by Django 3.2.7 on 2021-09-12 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcodes', '0008_postcode_measurement_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcode',
            old_name='measurement_choice',
            new_name='distance_unit',
        ),
    ]
