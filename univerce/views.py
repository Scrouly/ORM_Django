import random as rm

import django.db.utils as ddu
from django.shortcuts import render, get_list_or_404

from univerce.data_creation import students_data_creation as sdc
from univerce.models import *


def index(request):
    return render(request, 'labs/start.html')


def task1(request):
    students = Students.objects.all().filter(status='expelled')
    last_stud = students.order_by('-status_date')[:1]
    return render(request, 'labs/task1.html', {
        'students': students, 'last_stud': last_stud
    })


def stud_info(request, id_stud: int):
    get_list_or_404(Students, record_book_number=id_stud)
    student = Students.objects.get(record_book_number=id_stud)
    return render(request, 'labs/student_info.html', {
        'student': student
    })


def task2(request):
    subject_plan = Curriculum.objects.all()
    return render(request, 'labs/task2.html', {
        'subject_plan': subject_plan
    })


def curriculum_creation(request):
    subjects = ['Institutes', 'Programming technologies', 'Physical Culture', 'VDTSA',
                'Optimization of design solutions', 'Technical automation devices', 'Enterprise economy']
    rm.shuffle(subjects)
    status = ['approved', 'under consideration']
    Curriculum.objects.create(subject_one=subjects[0], subject_one_hours=rm.randint(20, 150),
                              subject_two=subjects[1], subject_two_hours=rm.randint(20, 150),
                              subject_three=subjects[2],
                              subject_three_hours=rm.randint(20, 150), subject_four=subjects[3],
                              subject_four_hours=rm.randint(20, 150), status=rm.choice(status))
    subject_plan = Curriculum.objects.all().order_by('-id')[:1]
    return render(request, 'labs/curriculum_creation.html', {
        'subject_plan': subject_plan
    })


def curriculum_for_group(request):
    groups = Groups.objects.filter(curriculum_code=None)
    all_groups = Groups.objects.all()
    all_cur = Curriculum.objects.all()
    stud_plan = []
    counter = 0
    for j in all_cur:
        stud_plan.append(j)
    rm.shuffle(stud_plan)

    if groups:
        for curriculum_co in groups:
            while True:
                try:
                    curriculum_co.curriculum_code = stud_plan[counter]
                    curriculum_co.save()
                except ddu.IntegrityError:
                    counter += 1
                else:
                    break
    return render(request, 'labs/curriculum_for_group.html', {
        'groups': groups, 'all_groups': all_groups})


def task3(request):
    studs = Students.objects.all().order_by('group_code')
    st = Students.objects.all()
    group = []
    year = []
    update_list = []
    for students in st:
        a = Groups.objects.filter(name=students.group_code)
        for i in a:
            gr = i.name.split('-')[0]
            if gr not in group:
                group.append(gr)
        ye = students.status_date.year
        if ye not in year:
            year.append(ye)
    year.sort()
    for i in range(len(group)):
        for j in range(len(year)):
            upd = Students.objects.filter(group_code__name__contains=group[i]).filter(status_date__year=year[j])
            if len(upd) < 20:
                for k in upd:
                    temp = upd[0]
                    if k.group_code != temp.group_code:
                        upd.update(group_code=upd[0].group_code)
                        update_list.append(upd)
                        break

    return render(request, 'labs/task3.html', {
        'st': studs, "update_list": update_list})


def add_student(request):
    student_list = sdc.get_name()
    city_list = sdc.get_city()
    address_list = sdc.get_address()
    sdc.get_telephone()
    group_code_list = []
    added_students_list = []
    groups_cods_list = Groups.objects.all()
    status_list = ("expelled","enlisted")
    for group_code in groups_cods_list:
        group_code_list.append(group_code)
    for i in range(len(student_list) - 5):
        student = Students.objects.create(group_code=rm.choice(groups_cods_list),
                                          record_book_number=rm.randint(10000, 15000),
                                          surname=student_list[i].split(" ")[0],
                                          name=student_list[i].split(" ")[1], patronymic=student_list[i].split(" ")[2],
                                          city=rm.choice(city_list), address=address_list[i],
                                          telephone=sdc.get_telephone(),status =rm.choice(status_list) )
        added_students_list.append(student)

    return render(request, 'labs/create_studs.html', {
        'added_students_list': added_students_list})
