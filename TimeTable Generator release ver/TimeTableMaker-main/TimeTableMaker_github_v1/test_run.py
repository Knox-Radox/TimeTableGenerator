import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","TimeTableMaker.settings")

import django
django.setup()

from TimeTableApp.models import TimeTable, Teachers
from TimeTableApp import models
'''

# def limit_choices_teachers(period):
#     limited_choice = []
#     already_used_choice = TimeTable.objects.values_list(period,flat=True) #returns id of the teacher already linked on that period
#     for teacher in Teachers.objects.all():
#         if teacher.id not in already_used_choice:
#             limited_choice.append(teacher)
#     return limited_choice


def limit_choices_teachers(period):
    return Teachers.objects.exclude(id__in=TimeTable.objects.values_list(f"{period}_id",flat=True))

# print(limit_choices_teachers('mon_1'))
# print(limit_choices_teachers('mon_1'))

print(TimeTable.section.field.choices)
print(list(TimeTable.objects.values_list('section',flat=True)))
#
def limit_choices_sections():
    limited_choice = []
    already_used_choice = list(TimeTable.objects.values_list('section',flat=True))
    for section in TimeTable.section.field.choices:
        if section[0] not in already_used_choice: # because section is a tuple  and already_used_choice is a list
            limited_choice.append(section)
    return limited_choice

print(limit_sections())
'''


'''
Instance = models.TimeTable.objects.get(pk=6)
print(Instance.mon_1)
'''

'''
def limit_choices_teachers_update_form_for_mon_1(obj_id):
    exclude =Teachers.objects.exclude(id__in=TimeTable.objects.values_list(f"mon_1_id",flat=True).exclude(id=TimeTable.objects.get(id=obj_id).mon_1_id))
    return exclude
# print(limit_choices_teachers_update_form_for_mon_1(4))
print()
# print(TimeTable.objects.get(id=4).mon_1_id)
# print(TimeTable.objects.values_list(f"mon_1_id",flat=True))
print()

# L = TimeTable.objects.values_list(f"mon_1_id",flat=True)
# L.exclude(id=int(TimeTable.objects.get(id=4).mon_1_id))
# print(L)
print()
print(TimeTable.objects.values_list(f"mon_1_id",flat=True).filter(id=Teachers.objects.))
# print(TimeTable.objects.values_list(f"mon_1_id",flat=True).exclude(id=TimeTable.objects.filter(id=TimeTable.objects.get(id=4).mon_1_id).values()))
# print(TimeTable.objects.values_list(f"mon_1_id",flat=True).exclude(id=TimeTable.objects.get(id=4).mon_1_id))
'''

def limit_mon_1():
    return Teachers.objects.exclude(id__in=TimeTable.objects.values_list('mon_1_id',flat=True))

# print(limit_mon_1())
#
# L = TimeTable.objects.values_list('mon_3_id',flat=True)
# print(L)
#
# print(TimeTable.objects.get(id=4).mon_1_id)
#
# print(Teachers.objects.get(id=TimeTable.objects.get(id=4).mon_1_id))
# print(Teachers.objects.get(id=TimeTable.objects.get(id=4).mon_1_id).id)
#
# id  = Teachers.objects.get(id=TimeTable.objects.get(id=4).mon_1_id).id
# L = list(L)
# L.remove(id)
# print(L)
#
# print("'''''''''")
# print(limit_mon_1())
# print()
# print(Teachers.objects.exclude(id__in=L))


def limit_choices_teachers_update_form_for_mon_1(obj_id):
    L = TimeTable.objects.values_list('mon_1_id',flat=True)
    id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_1_id).id
    L = list(L)
    L.remove(id)
    return Teachers.objects.exclude(id__in=L)

# print(limit_choices_teachers_update_form_for_mon_1(6))
'''Testing going on. Hope it works'''
#
# try:
#     id  = Teachers.objects.get(id=TimeTable.objects.get(id=9).mon_5_id).id
#     print(id)
# except models.Teachers.DoesNotExist:
#     print("Handled")
obj_id=9
L = TimeTable.objects.values_list('mon_5_id',flat=True)
L = list(L)
try:
    id  = Teachers.objects.get(id=TimeTable.objects.get(id=obj_id).mon_5_id).id
    L.remove(id)
except models.Teachers.DoesNotExist:
    pass
print(Teachers.objects.exclude(id__in=L))
