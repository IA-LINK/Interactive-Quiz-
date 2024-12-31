from django.urls import path
from .api_views import QuizListAPI
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/quizz/', views.admin_quiz_list, name='admin_quiz_list'),
    path('admin/quizz/add/', views.admin_add_quiz, name='admin_add_quiz'),
    path('admin/quizz/edit/<int:quiz_id>/', views.admin_edit_quiz, name='admin_edit_quiz'),
    path('admin/quizz/delete/<int:quiz_id>/', views.admin_delete_quiz, name='admin_delete_quiz'),
    #path('<int:quiz_id>/result/', views.quiz_result, name='quiz_result'),
    path('api/quizz/', QuizListAPI.as_view(), name='quiz_list_api'),
]

