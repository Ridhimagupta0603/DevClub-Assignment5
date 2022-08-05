from django.contrib import admin
from .models import Student,Instructor
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Student)
@admin.register(Instructor)

class userdata(ImportExportModelAdmin):
    pass