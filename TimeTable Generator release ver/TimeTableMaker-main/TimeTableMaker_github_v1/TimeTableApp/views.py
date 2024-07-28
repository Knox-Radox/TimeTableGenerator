from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from . import models
from . import forms
# Create your views here.

def limit_choices_teachers(period):
    return models.Teachers.objects.exclude(id__in=models.TimeTable.objects.values_list(f"{period}_id",flat=True))


class indexPage(TemplateView):
    template_name = 'TimeTableApp/inner_index.html'

'''TimeTable model views'''
class CreateTimeTable(CreateView):
    model = models.TimeTable
    form_class = forms.TimeTableForm
    template_name = 'TimeTableApp/TimeTable_model/create_timetable.html'
    success_url = reverse_lazy('TimeTableApp:inner_index')

class UpdateTimeTable(UpdateView):
    model = models.TimeTable
    form_class = forms.TimeTableUpdateForm
    template_name = 'TimeTableApp/TimeTable_model/update_timetable.html'
    success_url = reverse_lazy('TimeTableApp:timetable_list')

class DeleteTimeTable(DeleteView):
    model = models.TimeTable
    template_name = 'TimeTableApp/TimeTable_model/delete_timetable.html'
    success_url = reverse_lazy("TimeTableApp:timetable_list")

class TimeTableListView(ListView):
    model = models.TimeTable
    template_name = 'TimeTableApp/TimeTable_model/timetable_list.html'
    context_object_name = 'TimeTableList'

class TimeTableDetailView(DetailView):
    model = models.TimeTable
    template_name = 'TimeTableApp/TimeTable_model/timetable_detail.html'
    context_object_name = 'TimeTable'


'''Subjects model views'''
class SubjectsListView(ListView):
    model = models.Subjects
    template_name = 'TimeTableApp/Subjects_model/subject_list.html'
    context_object_name = 'subjects'

class SubjectsDetailView(DetailView):
    model = models.Subjects
    template_name = 'TimeTableApp/Subjects_model/subject_detail.html'
    context_object_name = 'subject'

class SubjectsCreateView(CreateView):
    model = models.Subjects
    fields = ('__all__')
    template_name = 'TimeTableApp/Subjects_model/subject_form.html'
    success_url = reverse_lazy('TimeTableApp:subject_list')

class SubjectsDeleteView(DeleteView):
    model = models.Subjects
    template_name = 'TimeTableApp/Subjects_model/subject_delete_form.html'
    success_url = reverse_lazy('TimeTableApp:subject_list')


'''Teachers model views'''
class TeachersListView(ListView):
    model = models.Teachers
    template_name = 'TimeTableApp/Teachers_model/teacher_list.html'
    context_object_name = 'teachers'

class TeachersDetailView(DetailView):
    model = models.Teachers
    template_name = 'TimeTableApp/Teachers_model/teacher_detail.html'
    context_object_name = 'teacher'

class TeachersCreateView(CreateView):
    model = models.Teachers
    fields = ('__all__')
    template_name = 'TimeTableApp/Teachers_model/teacher_form.html'
    success_url = reverse_lazy("TimeTableApp:teacher_list")

class TeachersUpdateView(UpdateView):
    model = models.Teachers
    fields = ('__all__')
    template_name = 'TimeTableApp/Teachers_model/teacher_update_form.html'
    success_url = reverse_lazy("TimeTableApp:teacher_list")

class TeachersDeleteView(DeleteView):
    model = models.Teachers
    template_name = 'TimeTableApp/Teachers_model/teacher_delete_form.html'
    success_url = reverse_lazy("TimeTableApp:teacher_list")
