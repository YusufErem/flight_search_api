# Generated by Django 5.0.6 on 2024-05-13 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Havaalanlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Ucuslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kalkis_zamani', models.DateTimeField()),
                ('donus_zamani', models.DateTimeField()),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kalkis_havaalani', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='kalkis_havaalanlari', to='flights.havaalanlari')),
                ('varis_havaalani', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='varis_havaalanlari', to='flights.havaalanlari')),
            ],
        ),
    ]
