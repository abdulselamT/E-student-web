# Generated by Django 2.2.12 on 2021-08-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_teacherarrangment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherarrangment',
            name='section',
        ),
        migrations.AddField(
            model_name='teacherarrangment',
            name='section',
            field=models.ManyToManyField(null=True, to='student.Section'),
        ),
    ]