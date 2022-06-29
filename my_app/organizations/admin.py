from django.contrib import admin
from organizations.models import Organization, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'status')
    list_filter = ('title', )


class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'estd', 'category', 'phone', 'status')
    list_filter = ('category', 'status')
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Organization, OrgAdmin)
