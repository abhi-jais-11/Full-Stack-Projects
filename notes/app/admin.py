from django.contrib import admin
from .models import *

# Register your models here.


class AdminNote(admin.ModelAdmin):
    list_display = ("title", "user_name", "date")


admin.site.register(Note, AdminNote)
