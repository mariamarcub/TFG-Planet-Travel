# Generated by Django 5.0.3 on 2024-05-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_remove_voyage_date_voyage_date_end_voyage_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='date_start',
            field=models.DateField(),
        ),
    ]