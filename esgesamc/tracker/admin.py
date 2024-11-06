# tracker/admin.py

from django.contrib import admin
from .models import EmissionData

admin.site.register(EmissionData)
