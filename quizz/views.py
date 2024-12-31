from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Option, Result
from .forms import QuizForm

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_option_id = form.cleaned_data.get(f'question_{question.id}')
                selected_option = Option.objects.get(id=selected_option_id)
                if selected_option.is_correct:
                    score += 1
            Result.objects.create(user=request.user, quiz=quiz, score=score)
            return redirect('quiz_result', quiz_id=quiz.id)
    else:
        form = QuizForm(questions=questions)
    return render(request, 'quizzes/take_quiz.html', {'quiz': quiz, 'form': form})

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = Result.objects.filter(user=request.user, quiz=quiz).first()
    return render(request, 'quizzes/quiz_result.html', {'quiz': quiz, 'result': result})
