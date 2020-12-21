# Generated by Django 3.1.4 on 2020-12-08 12:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0002_auto_20201208_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Attended', 'Attended'), ('Missed', 'Missed'), ('Cancelled', 'Cancelled')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
        migrations.AddField(
            model_name='booking',
            name='confirm_email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='surname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='time_in',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='time_out',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='system',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resort.booking'),
        ),
        migrations.AddField(
            model_name='system',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resort.customer'),
        ),
    ]