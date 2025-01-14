from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Question
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages

from .models import Subscriber
from django.db import IntegrityError

def About(request):
    return render(request, 'about.html')  

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            # Email already subscribed
            messages.warning(request, "You are already subscribed!")
        else:
            try:
                Subscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
            except IntegrityError:
                # Handle unexpected errors gracefully
                messages.error(request, "An error occurred. Please try again.")
        return redirect('home')
    return redirect('home')




def login_view(request):
    return render(request, 'login.html')

def Signup(request):
    if request.method=='POST':
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        data.save()
        return redirect('login')


    return render(request,'signup.html') 
   

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if  user is not None:
            auth.login(request,user)
            return redirect('home')

    return render(request,'login.html')


lst = []
question_total = []

def Home(request):
    lst.clear()
    question_total.clear()

    return render(request, 'home.html')


def quiz(request):
    obj = Question.objects.all()
    
    question_count = obj.count() * 5
    question_total = [question_count]
    paginator = Paginator(obj, 1)
    try:
        page_number = int(request.GET.get('page', '1'))
    except ValueError:
        page_number = 1
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'quiz.html', {'obj': obj, 'questions': page})


lst = []
anslist = []
answers = Question.objects.all()

for i in answers:
    anslist.append(i.answer)


def result(request):
    lst = [1, 2, 3]
    anslist = [1, 2, 3]
    score = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 5
    question_total_value = Question.objects.all().count()
    return render(request, 'result.html', {"score": score, 'question_total': question_total_value})

def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)