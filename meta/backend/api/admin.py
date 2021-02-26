from django.contrib import admin
from django.utils.safestring import mark_safe

from api.models import Profile, Skills


class MethodsInLine(admin.TabularInline):
    model = Profile.methods.through


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_photo']
    inlines = [MethodsInLine]
    exclude = ('methods',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo}" width="100px">')
        return '-'

    get_photo.short_description = 'Photo'


@admin.register(Skills)
class MethodAdmin(admin.ModelAdmin):
    list_display = ['title']

