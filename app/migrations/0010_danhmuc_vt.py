# Generated by Django 5.0.1 on 2024-01-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_danhmuc_sanpham_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='danhmuc',
            name='vt',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
