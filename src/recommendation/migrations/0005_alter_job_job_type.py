# Generated by Django 4.2.5 on 2023-11-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendation", "0004_alter_job_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("Full-Time", "Full-Time"),
                    ("Part-Time", "Part-Time"),
                    ("Contract", "Contract"),
                    ("Freelance", "Freelance"),
                ],
                default="Full-Time",
                max_length=20,
            ),
        ),
    ]
