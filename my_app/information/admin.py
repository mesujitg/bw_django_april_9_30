from django.contrib import admin
from django.template.defaultfilters import safe
from information.models import Section, Information
from import_export.admin import ImportExportModelAdmin


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')


class InfoAdmin(ImportExportModelAdmin):
    list_display = ('section', 'title', 'get_details', 'status')

    def get_details(self, obj):
        return safe(obj.details)


admin.site.register(Section, SectionAdmin)
admin.site.register(Information, InfoAdmin)
