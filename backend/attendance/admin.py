from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list = '__all__'


admin.site.register(Student, StudentAdmin)