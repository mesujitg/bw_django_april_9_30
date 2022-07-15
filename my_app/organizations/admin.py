from django.contrib import admin
from django.utils.html import format_html

from organizations.models import Organization, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'status')
    list_filter = ('title', )


class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'estd', 'category', 'phone', 'status')
    list_filter = ('category', 'status')
    search_fields = ('name', )

    def get_image(self, obj):
        return format_html(f'<img src="/media/{ obj.logo}" alt="" style="width: 100px; height:100px"')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Organization, OrgAdmin)
