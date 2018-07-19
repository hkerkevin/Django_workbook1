# Generated by Django 2.0.1 on 2018-01-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=200)),
                ('is_male', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('market_cap', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('superpower', models.CharField(max_length=100)),
                ('is_good', models.BooleanField()),
                ('is_male', models.BooleanField()),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]