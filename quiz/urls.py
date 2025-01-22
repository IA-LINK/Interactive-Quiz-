from django.urls import path

from webquizzy import settings
from . import views
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import RedirectView

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_page, name='start'),  # Homepage for the quiz app
    path('quiz/', views.quizz_view, name='quiz'),  # Renamed for clarity
    path('result/', views.quiz_result, name='quiz_result'),  # Simplified path
    path('submit/', views.submit_quiz, name='submit'),  # For submitting quizzes
    path('quizz', views.quizz_view, name='quiz'),
    path('login/', views.login_view, name='login'),
    path('profiles/<str:username>/', views.user_profiles, name='user_profiles'),
    path('profile.html', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('profile/leaderboard.html', views.leaderboard, name='leaderboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
]
