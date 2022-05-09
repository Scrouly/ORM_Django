# Generated by Django 4.0.4 on 2022-05-09 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univerce', '0009_alter_curriculum_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='status',
            field=models.CharField(blank=True, db_column='Status', default='created', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='status_date',
            field=models.DateField(auto_now=True, db_column='Status Date', null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(blank=True, default='expelled', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='status_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterModelTable(
            name='curriculum',
            table='curriculum',
        ),
    ]
