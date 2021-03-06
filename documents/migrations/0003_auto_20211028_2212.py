# Generated by Django 3.2.8 on 2021-10-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='checksum',
            field=models.CharField(max_length=2000, unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='classification',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.CharField(max_length=2000, unique=True),
        ),
    ]
