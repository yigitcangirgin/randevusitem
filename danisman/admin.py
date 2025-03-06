from django.contrib import admin
from .models import Danisman
# Register your models here.



class DanismanAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'specialization', 'fee', 'created_at')
    search_fields = ('full_name', 'specialization')
    list_filter = ('specialization',)
    ordering = ['full_name']

admin.site.register(Danisman , DanismanAdmin)