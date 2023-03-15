# Generated by Django 3.2.16 on 2023-03-07 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20230306_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='donor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.donor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor',
            field=models.ManyToManyField(blank=True, null=True, to='home.Donor'),
        ),
    ]