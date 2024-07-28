from django import forms
from . import models

from TimeTableApp.models import TimeTable, Teachers

'''
    A glitch in TimeTable model
    - no same teacher can teach two class at the same time - this overlapping issue is accounted for by limiting the choices in the forms
    but one can create overlap teacher in the timetable while creating the record manually in the admin

    Watch that out
'''


# my actual logic
# def limit_choices_teachers(period):
#     limited_choice = []
#     already_used_choice = TimeTable.objects.values_list(period,flat=True) #returns id of the teacher already linked on that period
#     for teacher in Teachers.objects.all():
#         if teacher.id not in already_used_choice:
#             limited_choice.append(teacher)
#     return limited_choice

# suggested logic
def limit_choices_teachers(period):
    return Teachers.objects.exclude(id__in=TimeTable.objects.values_list(f"{period}_id",flat=True))


'''Update Form limt choices'''
# Monday
def limit_choices_teachers_update_form_for_mon_1(obj_id):
    L = TimeTable.objects.values_list('mon_1_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_1_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_mon_2(obj_id):
    L = TimeTable.objects.values_list('mon_2_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_2_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_mon_3(obj_id):
    L = TimeTable.objects.values_list('mon_3_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_3_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_mon_4(obj_id):
    L = TimeTable.objects.values_list('mon_4_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_4_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_mon_5(obj_id):
    L = TimeTable.objects.values_list('mon_5_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_5_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)

#Tuesday
def limit_choices_teachers_update_form_for_tue_1(obj_id):
    L = TimeTable.objects.values_list('tue_1_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).tue_1_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_tue_2(obj_id):
    L = TimeTable.objects.values_list('tue_2_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).tue_2_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_tue_3(obj_id):
    L = TimeTable.objects.values_list('tue_3_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).tue_3_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_tue_4(obj_id):
    L = TimeTable.objects.values_list('tue_4_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).tue_4_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_tue_5(obj_id):
    L = TimeTable.objects.values_list('tue_5_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).tue_5_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)

#Wednesday
def limit_choices_teachers_update_form_for_wednes_1(obj_id):
    L = TimeTable.objects.values_list('wednes_1_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).wednes_1_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_wednes_2(obj_id):
    L = TimeTable.objects.values_list('wednes_2_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).wednes_2_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_wednes_3(obj_id):
    L = TimeTable.objects.values_list('wednes_3_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).wednes_3_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_wednes_4(obj_id):
    L = TimeTable.objects.values_list('wednes_4_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).wednes_4_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_wednes_5(obj_id):
    L = TimeTable.objects.values_list('wednes_5_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).wednes_5_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
#Thursday
def limit_choices_teachers_update_form_for_thurs_1(obj_id):
    L = TimeTable.objects.values_list('thurs_1_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).thurs_1_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_thurs_2(obj_id):
    L = TimeTable.objects.values_list('thurs_2_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).thurs_2_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_thurs_3(obj_id):
    L = TimeTable.objects.values_list('thurs_3_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).thurs_3_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_thurs_4(obj_id):
    L = TimeTable.objects.values_list('thurs_4_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).thurs_4_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_thurs_5(obj_id):
    L = TimeTable.objects.values_list('thurs_5_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).thurs_5_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
#Friday
def limit_choices_teachers_update_form_for_fri_1(obj_id):
    L = TimeTable.objects.values_list('fri_1_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).fri_1_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_fri_2(obj_id):
    L = TimeTable.objects.values_list('fri_2_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).fri_2_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_fri_3(obj_id):
    L = TimeTable.objects.values_list('fri_3_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).fri_3_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_fri_4(obj_id):
    L = TimeTable.objects.values_list('fri_4_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).fri_4_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)
def limit_choices_teachers_update_form_for_fri_5(obj_id):
    L = TimeTable.objects.values_list('fri_5_id',flat=True)
    L = list(L)
    try:
        id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).fri_5_id).id
        L.remove(id)
    except models.Teachers.DoesNotExist:
        pass
    return Teachers.objects.exclude(id__in=L)

class TimeTableForm(forms.ModelForm):
    class Meta():
        model = models.TimeTable
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(TimeTableForm, self).__init__(*args, **kwargs)

        self.fields['mon_1'].queryset = limit_choices_teachers('mon_1')
        self.fields['mon_2'].queryset = limit_choices_teachers('mon_2')
        self.fields['mon_3'].queryset = limit_choices_teachers('mon_3')
        self.fields['mon_4'].queryset = limit_choices_teachers('mon_4')
        self.fields['mon_5'].queryset = limit_choices_teachers('mon_5')

        self.fields['tue_1'].queryset = limit_choices_teachers('tue_1')
        self.fields['tue_2'].queryset = limit_choices_teachers('tue_2')
        self.fields['tue_3'].queryset = limit_choices_teachers('tue_3')
        self.fields['tue_4'].queryset = limit_choices_teachers('tue_4')
        self.fields['tue_5'].queryset = limit_choices_teachers('tue_5')

        self.fields['wednes_1'].queryset = limit_choices_teachers('wednes_1')
        self.fields['wednes_2'].queryset = limit_choices_teachers('wednes_2')
        self.fields['wednes_3'].queryset = limit_choices_teachers('wednes_3')
        self.fields['wednes_4'].queryset = limit_choices_teachers('wednes_4')
        self.fields['wednes_5'].queryset = limit_choices_teachers('wednes_5')

        self.fields['thurs_1'].queryset = limit_choices_teachers('thurs_1')
        self.fields['thurs_2'].queryset = limit_choices_teachers('thurs_2')
        self.fields['thurs_3'].queryset = limit_choices_teachers('thurs_3')
        self.fields['thurs_4'].queryset = limit_choices_teachers('thurs_4')
        self.fields['thurs_5'].queryset = limit_choices_teachers('thurs_5')

        self.fields['fri_1'].queryset = limit_choices_teachers('fri_1')
        self.fields['fri_2'].queryset = limit_choices_teachers('fri_2')
        self.fields['fri_3'].queryset = limit_choices_teachers('fri_3')
        self.fields['fri_4'].queryset = limit_choices_teachers('fri_4')
        self.fields['fri_5'].queryset = limit_choices_teachers('fri_5')

class TimeTableUpdateForm(forms.ModelForm):

    class Meta():
        model = models.TimeTable
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(TimeTableUpdateForm, self).__init__(*args, **kwargs)

        # Instance = models.TimeTable.objects.get(pk=self.instance.pk)
        # self.fields['mon_1'].initial = 'hello'

        self.fields['mon_1'].queryset = limit_choices_teachers_update_form_for_mon_1(self.instance.pk)
        self.fields['mon_2'].queryset = limit_choices_teachers_update_form_for_mon_2(self.instance.pk)
        self.fields['mon_3'].queryset = limit_choices_teachers_update_form_for_mon_3(self.instance.pk)
        self.fields['mon_4'].queryset = limit_choices_teachers_update_form_for_mon_4(self.instance.pk)
        self.fields['mon_5'].queryset = limit_choices_teachers_update_form_for_mon_5(self.instance.pk)

        self.fields['tue_1'].queryset = limit_choices_teachers_update_form_for_tue_1(self.instance.pk)
        self.fields['tue_2'].queryset = limit_choices_teachers_update_form_for_tue_2(self.instance.pk)
        self.fields['tue_3'].queryset = limit_choices_teachers_update_form_for_tue_3(self.instance.pk)
        self.fields['tue_4'].queryset = limit_choices_teachers_update_form_for_tue_4(self.instance.pk)
        self.fields['tue_5'].queryset = limit_choices_teachers_update_form_for_tue_5(self.instance.pk)

        self.fields['wednes_1'].queryset = limit_choices_teachers_update_form_for_wednes_1(self.instance.pk)
        self.fields['wednes_2'].queryset = limit_choices_teachers_update_form_for_wednes_2(self.instance.pk)
        self.fields['wednes_3'].queryset = limit_choices_teachers_update_form_for_wednes_3(self.instance.pk)
        self.fields['wednes_4'].queryset = limit_choices_teachers_update_form_for_wednes_4(self.instance.pk)
        self.fields['wednes_5'].queryset = limit_choices_teachers_update_form_for_wednes_5(self.instance.pk)

        self.fields['thurs_1'].queryset = limit_choices_teachers_update_form_for_thurs_1(self.instance.pk)
        self.fields['thurs_2'].queryset = limit_choices_teachers_update_form_for_thurs_2(self.instance.pk)
        self.fields['thurs_3'].queryset = limit_choices_teachers_update_form_for_thurs_3(self.instance.pk)
        self.fields['thurs_4'].queryset = limit_choices_teachers_update_form_for_thurs_4(self.instance.pk)
        self.fields['thurs_5'].queryset = limit_choices_teachers_update_form_for_thurs_5(self.instance.pk)

        self.fields['fri_1'].queryset = limit_choices_teachers_update_form_for_fri_1(self.instance.pk)
        self.fields['fri_2'].queryset = limit_choices_teachers_update_form_for_fri_2(self.instance.pk)
        self.fields['fri_3'].queryset = limit_choices_teachers_update_form_for_fri_3(self.instance.pk)
        self.fields['fri_4'].queryset = limit_choices_teachers_update_form_for_fri_4(self.instance.pk)
        self.fields['fri_5'].queryset = limit_choices_teachers_update_form_for_fri_5(self.instance.pk)
