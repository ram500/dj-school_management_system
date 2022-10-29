# Generated by Django 4.1.2 on 2022-10-26 12:35

import datetime
from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_student_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('registration_id', models.CharField(editable=sqlalchemy.sql.expression.false, max_length=6, primary_key=sqlalchemy.sql.expression.true, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_Registration', models.DateField(default=datetime.date(2022, 10, 26))),
                ('email', models.EmailField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('salary', models.BigIntegerField()),
                ('salary_paid', models.BigIntegerField(default=0)),
            ],
        ),
    ]