# Generated by Django 5.0.1 on 2024-01-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_date_of_birth_khachhang_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='khachhang',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]
