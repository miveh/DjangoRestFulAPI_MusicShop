# Generated by Django 3.2.5 on 2021-09-07 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='product.artist'),
        ),
    ]