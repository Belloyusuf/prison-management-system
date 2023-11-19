from django.contrib import admin
from . models import Prisoner, Onbail, Oncourt



@admin.register(Prisoner)
class PrisonerAdmin(admin.ModelAdmin):
    list_display = ["f_name", "l_name"]
    prepopulated_fields = {"slug": ("f_name", )}