# Generated by Django 5.1.6 on 2025-02-19 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='phone',
        ),
    ]
