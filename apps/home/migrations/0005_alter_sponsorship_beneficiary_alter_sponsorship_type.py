# Generated by Django 4.1.7 on 2023-08-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_donor_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='beneficiary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.beneficiary'),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.sponsorshiptype'),
        ),
    ]
