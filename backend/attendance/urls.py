# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/attendance', AttendanceViewSet, 'list')
router.register('api/student', StudentViewSet, 'student')

urlpatterns = router.urls