from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from . import models
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MeetupAdmin(admin.ModelAdmin):
    # to list the value in table start in db
    list_display = ('title', 'date', 'location')
    # to filter the value based on
    list_filter = ('title', 'date')
    # to automatically generate string of field based on another field
    prepopulated_fields = {'slug' : ('title',)}
    

admin.site.register(models.Meetup , MeetupAdmin)
admin.site.register(models.Location)
admin.site.register(models.Participant)
