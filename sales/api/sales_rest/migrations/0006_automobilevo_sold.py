# Generated by Django 4.0.3 on 2023-10-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0005_remove_automobilevo_color_remove_automobilevo_sold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilevo',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]