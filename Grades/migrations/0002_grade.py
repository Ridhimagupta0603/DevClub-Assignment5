# Generated by Django 4.0.6 on 2022-07-31 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('Grades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_grade', models.IntegerField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Grades.courses')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.student')),
            ],
        ),
    ]
