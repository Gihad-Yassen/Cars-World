# Generated by Django 5.2 on 2025-06-02 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_price_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('total_retal', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('status', models.CharField(blank=True, choices=[('rental', 'rental'), ('sold', 'sold'), ('availble', 'availble')], max_length=50, null=True)),
                ('active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.category')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.course')),
            ],
        ),
    ]
