# Generated by Django 3.2.5 on 2021-07-26 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
