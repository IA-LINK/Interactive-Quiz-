from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, HttpResponse
from .models import Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os

def newsletter_view(request):
    # Print the absolute path of the template to debug
    print(os.path.abspath('templates/subpage/newsletter.html'))
    return render(request, 'subpage/newsletter.html')


def newsletter_view(request):
    return render(request, 'subpage/newsletter.html')

# Signup View
def Signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        data = User.objects.create_user(
            first_name=first_name, last_name=last_name,
            email=email, username=username, password=password
        )
        data.save()
        return redirect('login')

    return render(request, 'signup.html')

# Login View
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

    return render(request, 'login.html')

# Home View
lst = []
question_total = []

def Home(request):
    lst.clear()
    question_total.clear()
    return render(request, 'home.html')

# Quiz View
def quiz(request):
    obj = Question.objects.all()
    question_count = obj.count() * 5
    question_total.append(question_count)
    paginator = Paginator(obj, 1)

    page = request.GET.get('page', 1)
    try:
        questions = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {'obj': obj, 'questions': questions})

# Result View
anslist = [q.answer for q in Question.objects.all()]

def result(request):
    score = sum(5 for i in range(len(lst)) if lst[i] == anslist[i])
    return render(request, 'result.html', {"score": score, 'question_total': question_total[0]})

# Save Answer View
def saveans(request):
    ans = request.GET.get('ans')
    if ans:
        lst.append(ans)
    return JsonResponse({'status': 'success'})

# Homepage View
def homepage(request):
    context = {'user': request.user}
    return render(request, 'homepage.html', context)

# About Us View
def about_us(request):
    context = {
        'team_members': [
            {'name': 'John Doe', 'role': 'Founder & CEO', 'image': 'https://via.placeholder.com/120'},
            {'name': 'Jane Smith', 'role': 'Lead Developer', 'image': 'https://via.placeholder.com/120'},
            {'name': 'Michael Lee', 'role': 'UX/UI Designer', 'image': 'https://via.placeholder.com/120'},
        ]
    }
    return render(request, 'about_us.html', context)

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Success case: Render the template with success message
            return render(request, 'subpage/newsletter.html', {'success': True})
        else:
            # Error case: Render the template with error message
            return render(request, 'subpage/newsletter.html', {'error': 'Please enter a valid email address.'})

