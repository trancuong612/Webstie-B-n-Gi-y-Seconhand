# Generated by Django 5.0.1 on 2024-01-18 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_name_khachhang_firstname_khachhang_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='khachhang',
            old_name='Date_of_birth',
            new_name='date_of_birth',
        ),
    ]
