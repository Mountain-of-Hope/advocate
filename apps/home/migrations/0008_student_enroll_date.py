# Generated by Django 4.1.7 on 2023-02-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_donor_email_student_community_student_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(null=True),
        ),
    ]
