# Generated by Django 3.1.1 on 2020-11-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_book_pacakges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pacakges',
        ),
        migrations.AddField(
            model_name='book',
            name='packages',
            field=models.CharField(choices=[('FULL DAY SPA', 'Full Day Spa'), ('HALF DAY SPA', 'Half Day Spa'), ('MOONLIGHT SPA', 'Moonlight Spa')], default='FULL DAY SPA', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='people',
            field=models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5'), ('SIX', '6'), ('SEVEN', '7'), ('EIGHT', '8'), ('NINE', '9'), ('TEN', '10')], default='ONE', max_length=100),
        ),
    ]