from django.contrib import admin
from .models import Courses,grade
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Courses)
@admin.register(grade)
class gradereg(ImportExportModelAdmin):
    pass