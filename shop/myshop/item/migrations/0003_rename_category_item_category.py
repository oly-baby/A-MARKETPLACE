# Generated by Django 3.2.23 on 2024-01-17 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20240114_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
    ]
