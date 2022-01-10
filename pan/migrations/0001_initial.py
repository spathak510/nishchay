# Generated by Django 3.0.9 on 2020-10-01 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('relative_name', models.CharField(blank=True, max_length=255)),
                ('dob', models.DateField(blank=True, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=150)),
                ('image_data', models.BinaryField()),
                ('deal_id', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pan_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pan_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]