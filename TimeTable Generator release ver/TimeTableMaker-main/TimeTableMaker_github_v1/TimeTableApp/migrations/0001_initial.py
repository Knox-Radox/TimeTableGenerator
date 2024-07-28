# Generated by Django 4.1.2 on 2023-06-27 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(choices=[('Maths', 'Maths'), ('English', 'English'), ('Computer', 'Computer'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics')], max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'), ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'), ('Grade 7', 'Grade 7'), ('Grade 8', 'Grade 8'), ('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10'), ('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')], max_length=256)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('fri_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_1_subject', to='TimeTableApp.subjects')),
                ('fri_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_2_subject', to='TimeTableApp.subjects')),
                ('fri_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_3_subject', to='TimeTableApp.subjects')),
                ('fri_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_4_subject', to='TimeTableApp.subjects')),
                ('fri_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri_5_subject', to='TimeTableApp.subjects')),
                ('mon_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_1_subject', to='TimeTableApp.subjects')),
                ('mon_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_2_subject', to='TimeTableApp.subjects')),
                ('mon_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_3_subject', to='TimeTableApp.subjects')),
                ('mon_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_4_subject', to='TimeTableApp.subjects')),
                ('mon_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mon_5_subject', to='TimeTableApp.subjects')),
                ('thurs_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thurs_1_subject', to='TimeTableApp.subjects')),
                ('thurs_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thurs_2_subject', to='TimeTableApp.subjects')),
                ('thurs_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thurs_3_subject', to='TimeTableApp.subjects')),
                ('thurs_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thurs_4_subject', to='TimeTableApp.subjects')),
                ('thurs_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thurs_5_subject', to='TimeTableApp.subjects')),
                ('tue_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_1_subject', to='TimeTableApp.subjects')),
                ('tue_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_2_subject', to='TimeTableApp.subjects')),
                ('tue_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_3_subject', to='TimeTableApp.subjects')),
                ('tue_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_4_subject', to='TimeTableApp.subjects')),
                ('tue_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tue_5_subject', to='TimeTableApp.subjects')),
                ('wednes_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_1_subject', to='TimeTableApp.subjects')),
                ('wednes_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_2_subject', to='TimeTableApp.subjects')),
                ('wednes_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_3_subject', to='TimeTableApp.subjects')),
                ('wednes_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_4_subject', to='TimeTableApp.subjects')),
                ('wednes_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wed_5_subject', to='TimeTableApp.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('teaches_for_class', models.CharField(choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'), ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'), ('Grade 7', 'Grade 7'), ('Grade 8', 'Grade 8'), ('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10'), ('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')], max_length=256)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='TimeTableApp.subjects')),
            ],
        ),
    ]