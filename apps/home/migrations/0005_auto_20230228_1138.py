# Generated by Django 3.2.16 on 2023-02-28 17:38

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('home', '0004_delete_paytest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('sponsor_address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
    ]
