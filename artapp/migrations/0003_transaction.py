# Generated by Django 5.1.7 on 2025-03-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0002_hiring_rename_booking_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed')], max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
