# Generated by Django 3.2.7 on 2021-09-14 11:57

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20210914_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='withcourse',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('grade', 'room_num')},
        ),
    ]
