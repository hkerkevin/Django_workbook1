# Generated by Django 2.0.1 on 2018-05-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_graffiti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
