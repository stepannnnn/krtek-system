# Generated by Django 5.1 on 2024-08-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='balance',
        ),
        migrations.AddField(
            model_name='guest',
            name='already_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='guest',
            name='to_pay',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
