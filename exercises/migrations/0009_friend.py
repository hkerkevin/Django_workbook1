# Generated by Django 2.0.1 on 2018-05-08 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_auto_20180419_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
