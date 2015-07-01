from django.contrib import admin
from bassculture.models.source import Source
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.printer import Printer
from bassculture.models.publisher import Publisher
from bassculture.models.tune import Tune
from django.forms import TextInput, Textarea
from django.db import models


@admin.register(Tune)
class TuneAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80%'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'edition', 'date']
    search_fields = ['full_title']
    filter_vertical = ['authors']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name']
    search_fields = ['surname', 'name']


@admin.register(Printer)
class PrintedAdmin(admin.ModelAdmin):
    search_fields = ['printer']


@admin.register(Publisher)
class PublishedAdmin(admin.ModelAdmin):
    search_fields = ['publisher']