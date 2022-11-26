# Generated by Django 3.2.15 on 2022-11-25 14:26

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Choose a boat'), ('1', 'k1'), ('2', 'k2'), ('3', 'k4'), ('4', 'c1'), ('5', 'c2'), ('6', 'c2'), ('7', "Va'a"), ('8', 'sup')], max_length=4, verbose_name='boat')),
            ],
        ),
        migrations.CreateModel(
            name='Effort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('length', models.PositiveIntegerField(verbose_name='Distance(m)')),
                ('time', models.PositiveIntegerField(verbose_name='Time(s)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('date', models.DateTimeField()),
                ('metric', models.CharField(choices=[('Overall Feeling', 'feeling'), ('Pulse', 'pulse'), ('Sickness', 'sickness'), ('Sleep Hours', 'sleep_hours'), ('Sleep Qualilty', 'sleep qualilty'), ('Soreness', 'soreness'), ('Stress', 'stress'), ('Weight Kilograms', 'weight_kg'), ("Yesterday's Training", 'yesterdays_training'), ('Fatigue', 'fatigue'), ('Menstruation', 'menstruation'), ('Injury', 'injury')], max_length=25)),
                ('value', models.FloatField()),
                ('score', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'metrics',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('uid', models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(1, 'AthleteInitials-Date dd/mm/yyy- session')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('crew', models.CharField(max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(1, 'Crew must be greater than 1 character')])),
                ('session_name', models.CharField(max_length=20, null=True)),
                ('session_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('conditions', models.CharField(blank=True, choices=[('0', 'calm'), ('1', 'ripples'), ('2', 'slight'), ('3', 'rough')], max_length=4, verbose_name='conditions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(1, 'Venue must be greater than 1 character')])),
            ],
        ),
    ]
