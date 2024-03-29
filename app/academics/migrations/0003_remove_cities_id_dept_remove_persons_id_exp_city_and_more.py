# Generated by Django 5.0.2 on 2024-03-11 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_cities_countries_departments_identification_types_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='id_dept',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='id_exp_city',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='id_ident_type',
        ),
        migrations.AlterField(
            model_name='departments',
            name='id_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.countries'),
        ),
        migrations.AlterField(
            model_name='students',
            name='id_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.persons'),
        ),
    ]
