from django.contrib import admin
from .models import *

@admin.register(Matc)
class MatcAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'first_team', 'second_team')
    list_filter = ('date',)
    search_fields = ('name', 'first_team__name', 'second_team__name')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )


