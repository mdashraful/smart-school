# Generated by Django 5.1.6 on 2025-02-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_reg_num_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
