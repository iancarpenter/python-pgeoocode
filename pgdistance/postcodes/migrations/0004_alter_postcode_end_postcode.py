# Generated by Django 3.2.7 on 2021-09-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcodes', '0003_alter_postcode_end_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcode',
            name='end_postcode',
            field=models.CharField(max_length=4),
        ),
    ]
