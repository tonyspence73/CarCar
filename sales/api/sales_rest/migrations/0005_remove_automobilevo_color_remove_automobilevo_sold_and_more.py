# Generated by Django 4.0.3 on 2023-10-25 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0004_alter_sale_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobilevo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='automobilevo',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='automobilevo',
            name='year',
        ),
    ]