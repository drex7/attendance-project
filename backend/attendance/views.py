from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


# class AttendanceView(viewsets.ModelViewSet):
#     serializer_class = AttendanceSerializer
#     queryset = Attendance.objects.all()