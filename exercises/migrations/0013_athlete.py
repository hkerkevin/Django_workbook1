# Generated by Django 2.0.1 on 2018-05-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sport', models.CharField(max_length=100)),
            ],
        ),
    ]