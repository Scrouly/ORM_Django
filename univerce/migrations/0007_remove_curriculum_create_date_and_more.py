# Generated by Django 4.0.4 on 2022-05-08 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univerce', '0006_alter_curriculum_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='status',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_four',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_four_hours',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_one_hours',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_three',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_three_hours',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_two',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='subject_two_hours',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='update_date',
        ),
    ]
