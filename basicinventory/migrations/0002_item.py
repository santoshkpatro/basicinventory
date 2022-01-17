# Generated by Django 4.0.1 on 2022-01-17 18:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('basicinventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('supplier_details', models.TextField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]