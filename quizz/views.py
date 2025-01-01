from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Option, Result
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.response import Response
from .forms import QuizForm, QuestionForm, OptionForm
from rest_framework.views import APIView
from .serializers import QuizSerializer
from django.contrib import messages


def home(request):
    return render(request, 'quizz/home.html')

def quiz_list(request):
    quizz = Quiz.objects.all()
    return render(request, 'quizz/quiz_list.html', {'quizz': quizz})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Restrict to staff users
def admin_delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        quiz.delete()
        messages.success(request, "Quiz deleted successfully!")
        return redirect('admin_quiz_list')

    return render(request, 'quizz/admin_confirm_delete.html', {'quiz': quiz})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Restrict to staff users
def admin_edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            quiz.title = title
            quiz.description = description
            quiz.save()
            messages.success(request, "Quiz updated successfully!")
            return redirect('admin_quiz_list')
        else:
            messages.error(request, "Both title and description are required.")

    return render(request, 'quizz/admin_edit_quiz.html', {'quiz': quiz})

def admin_edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            quiz.title = title
            quiz.description = description
            quiz.save()
            messages.success(request, "Quiz updated successfully!")
            return redirect('admin_quiz_list')
        else:
            messages.error(request, "Both title and description are required.")

    return render(request, 'quizz/admin_edit_quiz.html', {'quiz': quiz})

def admin_add_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            Quiz.objects.create(title=title, description=description)
            messages.success(request, "Quiz added successfully!")
            return redirect('admin_quiz_list')
        else:
            messages.error(request, "Both title and description are required.")

    return render(request, 'quizz/admin_add_quiz.html')


@login_required
@user_passes_test(lambda u: u.is_staff)  # Restrict to staff users
def admin_add_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            Quiz.objects.create(title=title, description=description)
            messages.success(request, "Quiz added successfully!")
            return redirect('admin_quiz_list')
        else:
            messages.error(request, "Both title and description are required.")

    return render(request, 'quizz/admin_add_quiz.html')

def admin_quiz_list(request):
    # Retrieve all quizz to display in the admin panel
    quizz = Quiz.objects.all()
    return render(request, 'quizz/admin_quiz_list.html', {'quizz': quizz})


@login_required
@user_passes_test(lambda u: u.is_staff)  # Restrict to staff users
def admin_quiz_list(request):
    quizz = Quiz.objects.all()
    return render(request, 'quizz/admin_quiz_list.html', {'quizz': quizz})


class QuizListAPI(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    current_question_index = request.session.get('current_question_index', 0)

    if current_question_index >= len(questions):
        # Calculate score and save result
        score = request.session.get('score', 0)
        Result.objects.create(user=request.user, quiz=quiz, score=score)
        del request.session['current_question_index']
        del request.session['score']
        return render(request, 'quizz/quiz_complete.html', {'quiz': quiz, 'score': score})

    question = questions[current_question_index]

    if request.method == 'POST':
        selected_option_id = request.POST.get('option')
        if selected_option_id:
            selected_option = Option.objects.get(id=selected_option_id)
            if selected_option.is_correct:
                request.session['score'] = request.session.get('score', 0) + 1
        request.session['current_question_index'] += 1
        return redirect('take_quiz', quiz_id=quiz.id)

    return render(request, 'quizz/take_quiz.html', {'quiz': quiz, 'question': question})

def admin_add_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz_form.save()
            return redirect('admin_quiz_list')
    else:
        quiz_form = QuizForm()
    return render(request, 'admin_add_quiz.html', {'quiz_form': quiz_form})

def admin_add_question(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_form = OptionForm(request.POST)
        if question_form.is_valid() and option_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            option_form.save(commit=False).question = question
            option_form.save()
            return redirect('admin_quiz_list')
    else:
        question_form = QuestionForm()
        option_form = OptionForm()
    return render(request, 'admin_add_question.html', {'question_form': question_form, 'option_form': option_form})
