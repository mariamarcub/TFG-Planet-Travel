# Generated by Django 5.0.3 on 2024-06-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_voyagethread_comment_thread_delete_forum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='voyagethread',
            options={'verbose_name_plural': 'VoyagesThreads'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]