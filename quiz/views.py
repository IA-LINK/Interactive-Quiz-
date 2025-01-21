from django.shortcuts import redirect, render # type: ignore

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz')  # Redirect to quiz page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# Quiz view (requires login)
@login_required
def quiz_view(request):
    quizzes = [
        {'title': 'Math Quiz', 'description': 'Test your math skills!', 'questions': 10},
        {'title': 'Science Quiz', 'description': 'Explore the wonders of science!', 'questions': 15},
        {'title': 'History Quiz', 'description': 'Dive into historical events!', 'questions': 12},
    ]
    return render(request, 'quiz.html', {'quizzes': quizzes})

def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    return render(request, 'profile/login.html')

def quiz_page(request):
    return render(request, 'quiz_page.html') 

def quiz_result(request):
    return render(request, 'quiz_result.html')

def submit_quiz(request):
    return redirect('quiz:quiz_result')

def submit_feedback(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        return redirect("thank_you")
    return render(request, "quiz_page.html")

# Quiz page view
def quizz_view(request):
    return render(request, 'quizz.html')

# Quiz result view

def quiz_result(request):
    correct_answers = {
        'lit_q1': 'a', 'lit_q2': 'a', 'lit_q3': 'b', 'lit_q4': 'b', 'lit_q5': 'a',
        'lit_q6': 'a', 'lit_q7': 'a', 'lit_q8': 'a', 'lit_q9': 'a', 'lit_q10': 'a',
        'hist_q1': 'a', 'hist_q2': 'b', 'hist_q3': 'a', 'hist_q4': 'a', 'hist_q5': 'a',
        'hist_q6': 'a', 'hist_q7': 'a', 'hist_q8': 'b', 'hist_q9': 'b', 'hist_q10': 'a',
        'math_q1': 'a', 'math_q2': 'a', 'math_q3': 'a', 'math_q4': 'b', 'math_q5': 'a',
        'math_q6': 'b', 'math_q7': 'c', 'math_q8': 'b', 'math_q9': 'b', 'math_q10': 'b',
        'geo_q1': 'b', 'geo_q2': 'b', 'geo_q3': 'c', 'geo_q4': 'a', 'geo_q5': 'b',
        'geo_q6': 'b', 'geo_q7': 'a', 'geo_q8': 'b', 'geo_q9': 'c', 'geo_q10': 'b',
    }
    
    total_questions = len(correct_answers)
    score = 0
    total_fail = 0

    for question, correct_answer in correct_answers.items():
        user_answer = request.POST.get(question)
        if user_answer == correct_answer:
            score += 1
        else:
            total_fail += 1

    # Calculate average score as a percentage
    average_score = (score / total_questions) * 100

    context = {
        'total_score': score,
        'total_fail': total_fail,
        'average_score': round(average_score, 2)
    }

    return render(request, 'quiz_result.html', context)

from django.shortcuts import render

def quiz_result(request):
    correct_answers = {
        'lit_q1': 'a', 'lit_q2': 'a', 'lit_q3': 'b', 'lit_q4': 'b', 'lit_q5': 'a',
        'lit_q6': 'a', 'lit_q7': 'a', 'lit_q8': 'a', 'lit_q9': 'a', 'lit_q10': 'a',
        'hist_q1': 'a', 'hist_q2': 'b', 'hist_q3': 'a', 'hist_q4': 'a', 'hist_q5': 'a',
        'hist_q6': 'a', 'hist_q7': 'a', 'hist_q8': 'b', 'hist_q9': 'b', 'hist_q10': 'a',
        'math_q1': 'a', 'math_q2': 'a', 'math_q3': 'a', 'math_q4': 'b', 'math_q5': 'a',
        'math_q6': 'b', 'math_q7': 'c', 'math_q8': 'b', 'math_q9': 'b', 'math_q10': 'b',
        'geo_q1': 'b', 'geo_q2': 'b', 'geo_q3': 'c', 'geo_q4': 'a', 'geo_q5': 'b',
        'geo_q6': 'b', 'geo_q7': 'a', 'geo_q8': 'b', 'geo_q9': 'c', 'geo_q10': 'b',
    }
    
    total_questions = len(correct_answers)
    score = 0
    total_fail = 0

    for question, correct_answer in correct_answers.items():
        user_answer = request.POST.get(question)
        if user_answer == correct_answer:
            score += 1
        else:
            total_fail += 1

    # Calculate average score as a percentage
    average_score = (score / total_questions) * 100

    context = {
        'total_score': score,
        'total_fail': total_fail,
        'average_score': round(average_score, 2)
    }

    return render(request, 'quiz_result.html', context)

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def login_view(request):
    return render(request, 'profile/login.html')

def signup_view(request):
    return render(request, 'sign.html')

def leaderboard_view(request):
    return render(request, 'leaderboard.html')

def quizz_view(request):
    return render(request, 'quizz.html')
