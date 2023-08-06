# Generated by Django 4.2.4 on 2023-08-06 17:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('federal_district', models.CharField(max_length=100)),
                ('region_type', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('area_type', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('city_type', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('settlement_type', models.CharField(max_length=100)),
                ('settlement', models.CharField(max_length=100)),
                ('kladr_id', models.CharField(max_length=100)),
                ('fias_id', models.CharField(max_length=100)),
                ('fias_level', models.CharField(max_length=100)),
                ('capital_marker', models.CharField(max_length=100)),
                ('okato', models.CharField(max_length=100)),
                ('oktmo', models.CharField(max_length=100)),
                ('tax_office', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('population', models.CharField(max_length=100)),
                ('foundation_year', models.CharField(max_length=100)),
            ],
        ),
    ]