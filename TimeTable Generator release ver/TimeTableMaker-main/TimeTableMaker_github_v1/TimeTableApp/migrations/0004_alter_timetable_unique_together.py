# Generated by Django 4.1.2 on 2023-06-27 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTableApp', '0003_alter_timetable_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('standard', 'mon_1'), ('standard', 'mon_2')},
        ),
    ]
