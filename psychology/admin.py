from django.contrib import admin
from psychology.models import Test, AnalyzingTest, Question, Variation, User


class AnalyzingTestInline(admin.TabularInline):
    model = AnalyzingTest
    extra = 3

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title',	{'fields': ['title']}),
        ('description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [AnalyzingTestInline]

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('order',	{'fields': ['order']}),
        ('description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [VariationInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(User)
# Register your models here.
