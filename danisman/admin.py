from django.contrib import admin
from .models import Danisman , Uygunluk
# Register your models here.



class DanismanAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'specialization', 'fee', 'created_at')
    search_fields = ('full_name', 'specialization')
    list_filter = ('specialization',)
    ordering = ['full_name']

admin.site.register(Danisman , DanismanAdmin)


class UygunlukAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('psychologist__name', 'day_of_week')

admin.site.register(Uygunluk, UygunlukAdmin)
