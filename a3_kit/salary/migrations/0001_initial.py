# Generated by Django 3.0.9 on 2020-10-12 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_id', models.CharField(max_length=255)),
                ('month1', models.CharField(blank=True, max_length=255)),
                ('month2', models.CharField(blank=True, max_length=255)),
                ('month3', models.CharField(blank=True, max_length=255)),
                ('month4', models.CharField(blank=True, max_length=255)),
                ('month5', models.CharField(blank=True, max_length=255)),
                ('month6', models.CharField(blank=True, max_length=255)),
                ('month7', models.CharField(blank=True, max_length=255)),
                ('sal_type', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_created_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.Customer_details')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]