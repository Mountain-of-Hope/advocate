# Generated by Django 4.1.7 on 2023-08-15 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_donor_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.group'),
        ),
    ]
