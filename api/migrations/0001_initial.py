# Generated by Django 2.2.5 on 2019-09-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('os', models.CharField(max_length=10)),
                ('impressions', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('installs', models.IntegerField()),
                ('spend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
