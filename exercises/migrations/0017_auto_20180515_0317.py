# Generated by Django 2.0.1 on 2018-05-15 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0016_task_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_Completed',
            new_name='is_completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='test',
        ),
    ]
