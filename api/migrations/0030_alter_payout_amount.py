# Generated by Django 5.0.2 on 2024-09-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_payout_amount_alter_payout_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payout',
            name='amount',
            field=models.IntegerField(default=0.3),
        ),
    ]
