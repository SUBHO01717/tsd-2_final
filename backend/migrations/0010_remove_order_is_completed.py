# Generated by Django 5.0.2 on 2024-02-09 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_order_quotation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_completed',
        ),
    ]