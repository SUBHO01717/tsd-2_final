# Generated by Django 4.1 on 2024-02-16 18:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_alter_job_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, default=1, max_length=300000),
            preserve_default=False,
        ),
    ]
