# Generated by Django 4.0.6 on 2022-08-04 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_instructor_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='instructor',
            table=None,
        ),
        migrations.AlterModelTable(
            name='student',
            table=None,
        ),
    ]
