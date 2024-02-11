# Generated by Django 5.0.2 on 2024-02-11 13:45

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
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('time_creat', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Женщина',
                'verbose_name_plural': 'Женщины',
            },
        ),
    ]