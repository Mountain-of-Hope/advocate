# Generated by Django 3.2.16 on 2023-03-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
