# Generated by Django 3.2.5 on 2021-07-15 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_milli_seconds_track_milliseconds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='compose',
            new_name='composer',
        ),
    ]