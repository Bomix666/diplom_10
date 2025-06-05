from django.contrib import admin
from .models import Category, Tag, Event, Source, Comment

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Source)
admin.site.register(Comment)
