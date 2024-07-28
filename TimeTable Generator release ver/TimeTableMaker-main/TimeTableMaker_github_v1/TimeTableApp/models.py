from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Subjects(models.Model):
    Subjects_available = (
        ('Maths','Maths'),
        ('English','English'),
        ('Computer','Computer'),
        ('Chemistry','Chemistry'),
        ('Physics','Physics'),
        ('Test Subject','Test Subject'),
    )
    subject_name = models.CharField(max_length = 256,choices = Subjects_available,unique=True)

    def  __str__(self):
        return str(self.subject_name)

class Teachers(models.Model):
    classes_available = (
        ('Grade 1','Grade 1'),
        ('Grade 2','Grade 2'),
        ('Grade 3','Grade 3'),
        ('Grade 4','Grade 4'),
        ('Grade 5','Grade 5'),
        ('Grade 6','Grade 6'),
        ('Grade 7','Grade 7'),
        ('Grade 8','Grade 8'),
        ('Grade 9','Grade 9'),
        ('Grade 10','Grade 10'),
        ('Grade 11','Grade 11'),
        ('Grade 12','Grade 12'),
    )

    name = models.CharField(max_length = 256)
    subject = models.ForeignKey(Subjects,on_delete=models.SET_NULL,null=True,related_name='teacher_subject')
    teaches_for_class = MultiSelectField(max_length=256,max_choices=5,choices=classes_available)

    def  __str__(self):
        return str(self.subject) + ' - ' + self.name + ' @ ' + str(self.teaches_for_class)

class TimeTable(models.Model):
    standard_choice = (
        ('Grade 1','Grade 1'),
        ('Grade 2','Grade 2'),
        ('Grade 3','Grade 3'),
        ('Grade 4','Grade 4'),
        ('Grade 5','Grade 5'),
        ('Grade 6','Grade 6'),
        ('Grade 7','Grade 7'),
        ('Grade 8','Grade 8'),
        ('Grade 9','Grade 9'),
        ('Grade 10','Grade 10'),
        ('Grade 11','Grade 11'),
        ('Grade 12','Grade 12'),
    )

    section_choice = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )

    standard = models.CharField(max_length=256,choices=standard_choice)
    section = models.CharField(max_length=1,choices=section_choice)

    mon_1 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='mon_1_subject_teacher')
    mon_2 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='mon_2_subject_teacher')
    mon_3 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='mon_3_subject_teacher')
    mon_4 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='mon_4_subject_teacher')
    mon_5 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='mon_5_subject_teacher')

    tue_1 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='tue_1_subject_teacher')
    tue_2 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='tue_2_subject_teacher')
    tue_3 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='tue_3_subject_teacher')
    tue_4 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='tue_4_subject_teacher')
    tue_5 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='tue_5_subject_teacher')

    wednes_1 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='wed_1_subject_teacher')
    wednes_2 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='wed_2_subject_teacher')
    wednes_3 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='wed_3_subject_teacher')
    wednes_4 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='wed_4_subject_teacher')
    wednes_5 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='wed_5_subject_teacher')

    thurs_1 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='thurs_1_subject_teacher')
    thurs_2 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='thurs_2_subject_teacher')
    thurs_3 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='thurs_3_subject_teacher')
    thurs_4 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='thurs_4_subject_teacher')
    thurs_5 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='thurs_5_subject_teacher')

    fri_1 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='fri_1_subject_teacher')
    fri_2 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='fri_2_subject_teacher')
    fri_3 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='fri_3_subject_teacher')
    fri_4 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='fri_4_subject_teacher')
    fri_5 = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,related_name='fri_5_subject_teacher')


    def  __str__(self):
        return self.standard+' '+self.section+ ' '+ 'TimeTable'

    # This works from one particular standard, but if some teachers take class for two grades , then you have 'ForeignKey'
    # the 'class they take' here and set unique_together constraint - hope it works
    class Meta():
        unique_together = [
        ['standard','section'],

        ['standard','mon_1'],
        ['standard','mon_2'],
        ['standard','mon_3'],
        ['standard','mon_4'],
        ['standard','mon_5'],

        ['standard','tue_1'],
        ['standard','tue_2'],
        ['standard','tue_3'],
        ['standard','tue_4'],
        ['standard','tue_5'],

        ['standard','wednes_1'],
        ['standard','wednes_2'],
        ['standard','wednes_3'],
        ['standard','wednes_4'],
        ['standard','wednes_5'],

        ['standard','thurs_1'],
        ['standard','thurs_2'],
        ['standard','thurs_3'],
        ['standard','thurs_4'],
        ['standard','thurs_5'],

        ['standard','fri_1'],
        ['standard','fri_2'],
        ['standard','fri_3'],
        ['standard','fri_4'],
        ['standard','fri_5'],
        ]

# def limit_choices_teachers(period):
#     limited_choice = []
#     already_used_choice = TimeTable.objects.value_list(period,flat=True)
#     for i in Teachers.objects.all:
#         if i not in already_used_choice:
#             limited_choice.append(i)
#     return limited_choice
