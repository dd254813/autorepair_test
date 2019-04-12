from django.contrib import admin
from app.models import Worker, Schedule, Customer


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'time_m', 'customer')
    list_filter = ['worker', 'date', 'time_m']


admin.site.register(Worker)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Customer)
