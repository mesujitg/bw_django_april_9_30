from django.contrib import admin
from applications.models import Application


class AppAdmin(admin.ModelAdmin):
    list_display = ('apply_date', 'user_id', 'job_id', 'status')


admin.site.register(Application, AppAdmin)
