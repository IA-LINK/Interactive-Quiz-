from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_page, name='start'),  # Homepage for the quiz app
    path('quiz/', views.quizz_view, name='quiz'),  # Renamed for clarity
    path('result/', views.quiz_result, name='quiz_result'),  # Simplified path
    path('submit/', views.submit_quiz, name='submit'),  # For submitting quizzes
    path('quizz', views.quizz_view, name='quiz'),
]
