# Generated by Django 5.0.3 on 2024-06-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pics/'),
        ),
    ]