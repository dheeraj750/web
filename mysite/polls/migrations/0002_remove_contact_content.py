# Generated by Django 4.0 on 2021-12-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
    ]
