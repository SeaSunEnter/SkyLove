# Generated by Django 5.0.6 on 2024-05-10 09:43

import django.db.models.deletion
import djmoney.models.fields
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'AssetCategory',
            },
        ),
        migrations.CreateModel(
            name='AssetUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'AssetUnit',
            },
        ),
        migrations.CreateModel(
            name='DeliveryTmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.SmallIntegerField(null=True)),
                ('customer_name', models.CharField(max_length=40, null=True)),
                ('treatment_id', models.SmallIntegerField(null=True)),
                ('treatment_name', models.CharField(max_length=64, null=True)),
                ('asset_id', models.SmallIntegerField(null=True)),
                ('asset_name', models.CharField(max_length=80, null=True)),
                ('asset_price_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('VND', 'VN ₫')], default='VND', editable=False, max_length=3, null=True)),
                ('asset_price', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='VND', max_digits=16, null=True)),
                ('quantity', models.SmallIntegerField(null=True)),
                ('paid_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('VND', 'VN ₫')], default='VND', editable=False, max_length=3, null=True)),
                ('paid', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='VND', max_digits=16, null=True)),
            ],
            options={
                'db_table': 'DeliveryTmp',
            },
        ),
        migrations.CreateModel(
            name='InventoryTmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeI', models.DateTimeField(null=True)),
                ('input', models.SmallIntegerField(null=True)),
                ('asset_id', models.SmallIntegerField(null=True)),
                ('asset_name', models.CharField(max_length=80, null=True)),
                ('category_id', models.SmallIntegerField(null=True)),
                ('category_name', models.CharField(max_length=32, null=True)),
                ('timeO', models.DateTimeField(null=True)),
                ('output', models.SmallIntegerField(null=True)),
                ('treatment', models.SmallIntegerField(null=True)),
                ('stock', models.SmallIntegerField(null=True)),
            ],
            options={
                'db_table': 'InventoryTmp',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mobile', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=125)),
                ('address', models.TextField(default='', max_length=100)),
                ('taxcode', models.CharField(max_length=32)),
                ('nubank', models.CharField(default='0123456789ABCDEF', max_length=16)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='Supplier')),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('purchase_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('VND', 'VN ₫')], default='VND', editable=False, max_length=3)),
                ('purchase', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='VND', max_digits=16)),
                ('unitINOUT', models.IntegerField(default=1)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('VND', 'VN ₫')], default='VND', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='VND', max_digits=16)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='Inventory')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.assetcategory')),
                ('unitIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnitIN', to='inventory.assetunit')),
                ('unitOUT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnitOUT', to='inventory.assetunit')),
            ],
            options={
                'db_table': 'Asset',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idIO', models.IntegerField()),
                ('quantityIO', models.SmallIntegerField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.asset')),
            ],
            options={
                'db_table': 'Inventory',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeI', models.DateTimeField(auto_now_add=True)),
                ('userID', models.SmallIntegerField()),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'db_table': 'Purchase',
            },
        ),
    ]