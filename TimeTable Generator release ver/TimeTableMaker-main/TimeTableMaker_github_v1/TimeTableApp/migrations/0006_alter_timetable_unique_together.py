# Generated by Django 4.1.2 on 2023-06-29 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTableApp', '0005_alter_timetable_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('standard', 'thurs_2'), ('standard', 'mon_5'), ('standard', 'wednes_1'), ('standard', 'tue_4'), ('standard', 'thurs_4'), ('standard', 'thurs_5'), ('standard', 'mon_4'), ('standard', 'thurs_3'), ('standard', 'fri_1'), ('standard', 'wednes_5'), ('standard', 'tue_1'), ('standard', 'section'), ('standard', 'wednes_3'), ('standard', 'mon_2'), ('standard', 'tue_3'), ('standard', 'mon_3'), ('standard', 'fri_4'), ('standard', 'mon_1'), ('standard', 'fri_2'), ('standard', 'tue_2'), ('standard', 'tue_5'), ('standard', 'thurs_1'), ('standard', 'wednes_2'), ('standard', 'fri_3'), ('standard', 'wednes_4'), ('standard', 'fri_5')},
        ),
    ]