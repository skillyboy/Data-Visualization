# Generated by Django 4.1 on 2023-04-19 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_data_country_alter_data_impact_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'managed': True, 'verbose_name': 'data', 'verbose_name_plural': 'datum'},
        ),
        migrations.AlterModelTable(
            name='data',
            table='data',
        ),
    ]