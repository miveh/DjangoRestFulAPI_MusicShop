# Generated by Django 3.2.5 on 2021-07-15 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_customer_is_active'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField()),
                ('billing_address', models.CharField(blank=True, max_length=70, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=40, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=40, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=40, null=True)),
                ('billing_postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('total', models.BigIntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment.invoice')),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.track')),
            ],
        ),
    ]
