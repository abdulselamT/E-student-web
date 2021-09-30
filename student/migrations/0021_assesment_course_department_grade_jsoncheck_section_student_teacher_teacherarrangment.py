# Generated by Django 3.2.7 on 2021-09-14 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0020_auto_20210914_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('logo', models.ImageField(default='profile1.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jsoncheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=67, null=True)),
                ('exam', jsonfield.fields.JSONField(default={}, null=True)),
                ('total', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.IntegerField(null=True)),
                ('withcourse', jsonfield.fields.JSONField(default={})),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('propic', models.ImageField(default='profile1.jpg', null=True, upload_to='')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('ministry_result', models.FloatField(max_length=200, null=True)),
                ('matric_result', models.FloatField(blank=True, max_length=200, null=True)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_phone_number', models.CharField(max_length=200, null=True)),
                ('propic', models.ImageField(default='profile1.jpg', null=True, upload_to='')),
                ('enroll_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.grade')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=40, null=True, unique=True)),
                ('course_name', models.CharField(max_length=200, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.department')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.grade')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherArrangment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.course')),
                ('section', models.ManyToManyField(to='student.Section')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
            options={
                'unique_together': {('course', 'teacher')},
            },
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asgt', jsonfield.fields.JSONField(default={})),
                ('mid', models.FloatField(null=True)),
                ('final', models.FloatField(null=True)),
                ('result', models.FloatField(null=True)),
                ('finished', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.course')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.section')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
            options={
                'unique_together': {('course', 'student')},
            },
        ),
    ]