# Generated by Django 3.2.5 on 2021-07-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='is_active',
        ),
    ]
