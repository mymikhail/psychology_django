from django.contrib import admin
from psychology.models import Test, AnalyzingTest


class AnalyzingTestInline(admin.StackedInline):
    model = AnalyzingTest
    extra = 3

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Название теста',	{'fields': ['title']}),
        ('Описание', 		{'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [AnalyzingTestInline]

admin.site.register(Test, TestAdmin)
# Register your models here.
