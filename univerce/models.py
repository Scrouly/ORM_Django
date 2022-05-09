from datetime import date
from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.

class Groups(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=50)
    code = models.AutoField(db_column='Code', primary_key=True)
    data = models.DateField(db_column='Data')
    curriculum_code = models.OneToOneField('Curriculum', models.SET_NULL, null=True)
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True,
                              default="created")
    status_date = models.DateField(db_column='Status Date', blank=True, null=True,
                                   auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'groups'


class Students(models.Model):
    group_code = models.ForeignKey(Groups, models.DO_NOTHING, db_column='Group Code')
    record_book_number = models.BigIntegerField(unique=True, primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    telephone = models.CharField(max_length=30)
    status = models.CharField(max_length=50, blank=True, null=True, default='enlisted')
    status_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def get_url(self):
        return reverse('student_inf', args=[self.record_book_number])

    def __str__(self):
        return self.surname

    class Meta:
        db_table = 'students'


class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    subject_one = models.CharField(max_length=50, blank=True, null=True)
    subject_one_hours = models.IntegerField(blank=True, null=True)
    subject_two = models.CharField(max_length=50, blank=True, null=True)
    subject_two_hours = models.IntegerField(blank=True, null=True)
    subject_three = models.CharField(max_length=50, blank=True, null=True)
    subject_three_hours = models.IntegerField(blank=True, null=True)
    subject_four = models.CharField(max_length=50, blank=True, null=True)
    subject_four_hours = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, default="approved")
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'curriculum'
