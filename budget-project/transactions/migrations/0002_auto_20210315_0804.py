# Generated by Django 3.1.7 on 2021-03-15 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Recurring',
        ),
    ]
