# Generated by Django 3.2.16 on 2023-03-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_church_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('Check', 'Check'), ('Online', 'Online')], default='Check', max_length=10),
        ),
    ]
