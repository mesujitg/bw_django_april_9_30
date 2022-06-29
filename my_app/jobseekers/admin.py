from django.contrib import admin
from jobseekers.models import JobSeeker


class JSAdmin(admin.ModelAdmin):
    list_display = ('user', 'objective', 'qualification', 'status')


admin.site.register(JobSeeker, JSAdmin)
