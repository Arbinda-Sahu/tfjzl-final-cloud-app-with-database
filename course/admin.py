from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.admin import TabularInline, ModelAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class QuestionInline(TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(ModelAdmin):
    list_display = ('question_text',)
    inlines = [ChoiceInline]


class LessonAdmin(ModelAdmin):
    list_display = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
