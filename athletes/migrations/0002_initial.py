# Generated by Django 3.2.15 on 2022-11-18 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='athlete',
            field=models.ManyToManyField(to='profiles.Athlete'),
        ),
        migrations.AddField(
            model_name='session',
            name='boat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.boattype'),
        ),
        migrations.AddField(
            model_name='session',
            name='coach',
            field=models.ManyToManyField(to='profiles.Coach'),
        ),
        migrations.AddField(
            model_name='session',
            name='team',
            field=models.ManyToManyField(to='profiles.Team'),
        ),
        migrations.AddField(
            model_name='session',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.venue'),
        ),
        migrations.AddField(
            model_name='metrics',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.athlete'),
        ),
        migrations.AddField(
            model_name='effort',
            name='session',
            field=models.ManyToManyField(to='athletes.Session'),
        ),
    ]