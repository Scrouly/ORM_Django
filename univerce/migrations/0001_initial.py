# Generated by Django 4.0.4 on 2022-05-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('code', models.AutoField(db_column='Code', primary_key=True, serialize=False)),
                ('data', models.DateField(db_column='Data')),
                ('kod_plana', models.IntegerField(db_column='Kod Plana')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('status_date', models.DateField(blank=True, db_column='Status Date', null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]