# Generated by Django 3.1.7 on 2021-03-15 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_recurring_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurring',
            name='type',
        ),
    ]
