from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Option, Result
from .forms import QuizForm, QuestionForm, OptionForm


def home(request):
    return render(request, 'home.html')


# List all quizz
@login_required
def admin_quiz_list(request):
    quizz = Quiz.objects.all()
    return render(request, 'admin/quiz_list.html', {'quizz': quizz})

# Add a new quiz
@login_required
def admin_add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_quiz_list')
    else:
        form = QuizForm()
    return render(request, 'admin/add_quiz.html', {'form': form})

# Edit a quiz
@login_required
def admin_edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('admin_quiz_list')
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'admin/edit_quiz.html', {'form': form, 'quiz': quiz})

# Delete a quiz
@login_required
def admin_delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('admin_quiz_list')
