from django.urls import path, include
from .api_views import QuizListAPI
from quizz import views  # Use only one import for views

urlpatterns = [
    # Root path
    path('', views.home, name='home'),

    # Admin quiz management paths
    path('admin/quizz/', views.admin_quiz_list, name='admin_quiz_list'),
    path('admin/quizz/add/', views.admin_add_quiz, name='admin_add_quiz'),
    path('admin/quizz/edit/<int:quiz_id>/', views.admin_edit_quiz, name='admin_edit_quiz'),
    path('admin/quizz/delete/<int:quiz_id>/', views.admin_delete_quiz, name='admin_delete_quiz'),

    # Quiz list API
    path('api/quizz/', QuizListAPI.as_view(), name='quiz_list_api'),

    # Quiz list view
    path('quizz/', views.quiz_list, name='quiz_list'),
]
