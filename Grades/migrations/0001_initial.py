# Generated by Django 4.0.6 on 2022-07-31 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('credit', models.PositiveSmallIntegerField(default=3)),
                ('a', models.PositiveSmallIntegerField(default=80)),
                ('b', models.PositiveSmallIntegerField(default=60)),
                ('c', models.PositiveSmallIntegerField(default=40)),
                ('d', models.PositiveSmallIntegerField(default=20)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Users.instructor')),
                ('students', models.ManyToManyField(to='Users.student')),
            ],
        ),
    ]
