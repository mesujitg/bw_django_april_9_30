from django.contrib import admin
from jobs.models import Job
from import_export.admin import ImportExportModelAdmin


class JobAdmin(ImportExportModelAdmin):
    list_display = ('title', 'type', 'category', 'level', 'salary', 'organization')
    list_filter = ('type', 'category')
    search_fields = ('title',)
    radio_fields = {'type': admin.HORIZONTAL}


admin.site.register(Job, JobAdmin)
