# Generated by Django 5.1.5 on 2025-03-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='available_time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
