# Generated by Django 3.1.1 on 2021-02-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analyze', '0002_delete_table_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_customer_month_kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=250)),
                ('account_number', models.CharField(max_length=250)),
            ],
        ),
    ]
