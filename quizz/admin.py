from django.contrib import admin
from .models import Quiz, Question, Option, Result

# Inline admin to manage options within the question admin
class OptionInline(admin.TabularInline):
    model = Option
    extra = 3  # Number of empty option fields to display by default

# Admin customization for Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')  # Fields to display in the admin list view
    inlines = [OptionInline]  # Add options inline within the question admin

# Admin customization for Quiz
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Fields to display in the admin list view
    search_fields = ('title',)  # Search bar for quizzes

# Admin customization for Result
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'date_taken')  # Fields to display in the admin list view
    list_filter = ('quiz', 'date_taken')  # Filter by quiz and date taken
    search_fields = ('user__username', 'quiz__title')  # Search bar for results

# Register models with their respective admin configurations
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
