# Generated by Django 3.1.1 on 2020-11-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20201101_1132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Booking',
        ),
    ]
