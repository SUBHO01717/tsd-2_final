# Generated by Django 4.1 on 2024-02-19 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_quotation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='email',
        ),
    ]
