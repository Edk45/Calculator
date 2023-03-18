from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub-date', 'question-text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)