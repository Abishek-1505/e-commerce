# Generated by Django 4.1.3 on 2022-11-27 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, limit_choices_to={'address_type': 'ship'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.customeraddress'),
        ),
    ]
