# Generated by Django 4.1.7 on 2023-02-28 18:02

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('home', '0006_auto_20230228_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='community',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
    ]
