# Generated by Django 3.1.1 on 2020-12-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_roomcategory_beds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='room_category',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Hollywood Twin Room', 'Hollywood Twin Room'), ('Cabana', 'Cabana'), ('Studio', 'Studio'), ('Suite', 'Suite')], max_length=100, null=True),
        ),
    ]