# Generated by Django 2.0.1 on 2018-04-19 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_blog_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog_data',
            new_name='Blog',
        ),
    ]
