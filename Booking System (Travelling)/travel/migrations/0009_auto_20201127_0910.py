# Generated by Django 3.1.1 on 2020-11-27 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_contact_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]