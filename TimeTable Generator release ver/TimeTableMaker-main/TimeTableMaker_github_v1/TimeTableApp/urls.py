from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'TimeTableApp'

urlpatterns = [
    path('',views.indexPage.as_view(),name='inner_index'),
    path('create_time_table/',views.CreateTimeTable.as_view(),name='create_time_table'),
    path('timetable_list/',views.TimeTableListView.as_view(),name='timetable_list'),
    path('timetable_list/<int:pk>/timetable_detail/',views.TimeTableDetailView.as_view(),name='timetable_detail'),
    path('timetable_list/<int:pk>/update_timetable/',views.UpdateTimeTable.as_view(),name='update_timetable'),
    path('timetable_list/<int:pk>/delete_timetable/',views.DeleteTimeTable.as_view(),name='delete_timetable'),

    path('subjects_list/',views.SubjectsListView.as_view(),name='subject_list'),
    path('subjects_list/<int:pk>/subjects_detail/',views.SubjectsDetailView.as_view(),name='subject_detail'),
    path('subjects_list/add_subject/',views.SubjectsCreateView.as_view(),name='create_subject'),
    path('subjects_list/<int:pk>/delete_subject/',views.SubjectsDeleteView.as_view(),name='delete_subject'),

    path('teachers/',views.TeachersListView.as_view(),name = 'teacher_list'),
    path('teachers/<int:pk>/teacher_detail/',views.TeachersDetailView.as_view(),name = 'teacher_detail'),
    path('teachers/create_teacher_profile/',views.TeachersCreateView.as_view(),name = 'create_teacher'),
    path('teachers/<int:pk>/update_teacher_profile/',views.TeachersUpdateView.as_view(),name='update_teacher'),
    path('teachers/<int:pk>/delete_teacher_profile/',views.TeachersDeleteView.as_view(),name='delete_teacher'),
]
