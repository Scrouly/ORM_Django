from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('task1/<int:id_stud>/', stud_info, name='student_inf'),
    path('task1/', task1, name='task_1'),
    path('task2/', task2, name='task_2'),
    path('task2/create/', curriculum_creation, name='create_curriculum'),
    path('task2/groups/', curriculum_for_group, name='add_curriculum'),
    path('task3/', task3, name='task_3'),
    path('create_student/', add_student,name='create_student')


]
