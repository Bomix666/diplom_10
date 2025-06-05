from django.contrib import admin
from .models import Category, Tag, Event, Source, Comment

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'region', 'status', 'created_at')
    list_filter = ('status', 'categories', 'region', 'date')
    search_fields = ('title', 'description', 'region')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Source)
admin.site.register(Comment)
