# Generated by Django 4.2.5 on 2024-03-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommendation", "0012_job_industry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
