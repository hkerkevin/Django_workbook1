# Generated by Django 2.0.1 on 2018-06-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0018_task_ajax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
