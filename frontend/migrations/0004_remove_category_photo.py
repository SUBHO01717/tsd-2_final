# Generated by Django 5.0.2 on 2024-02-09 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_subcategory_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
    ]