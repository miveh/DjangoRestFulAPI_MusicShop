# Generated by Django 3.2.5 on 2021-07-15 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_media_type_track_mediatype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='milli_seconds',
            new_name='milliseconds',
        ),
    ]
