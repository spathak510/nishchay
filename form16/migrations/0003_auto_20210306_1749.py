# Generated by Django 3.1.1 on 2021-03-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form16', '0002_info_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='challans',
            name='assessment_year',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='partb',
            name='assessment_year',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='quarters',
            name='assessment_year',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]