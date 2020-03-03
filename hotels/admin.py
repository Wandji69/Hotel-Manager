from django.contrib import admin

from .models import Room, Hotel


class RoomInline(admin.StackedInline):
    model = Room
    extra = 2


class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['desc_text']}),
        ('Date information', {'fields': ['act_date'], 'classes': ['collapse']}),
    ]
    inlines = [RoomInline]

    list_display = ('desc_text', 'act_date', 'active_date')
    list_filter = ['act_date']
    search_fields = ['desc_text']

admin.site.register(Hotel, HotelAdmin)