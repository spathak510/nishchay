# Generated by Django 3.0.9 on 2020-12-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20201012_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
