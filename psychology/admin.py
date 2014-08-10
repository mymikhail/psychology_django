from django.contrib import admin
from psychology.models import Test, AnalyzingTest


class AnalyzingTestInline(admin.TabularInline):
    model = AnalyzingTest
    extra = 3

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title',	{'fields': ['title']}),
        ('description', 		{'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [AnalyzingTestInline]

admin.site.register(Test, TestAdmin)
# Register your models here.
