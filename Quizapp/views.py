from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Question  # Add this import statement at the top of your views.
from django.core.paginator import Paginator


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
   

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if  user is not None:
            auth.login(request,user)
            return redirect('home')

    return render(request,'Login.html')


def Home(request):
    lst.clear()
    question_total.clear()
    return render(request,'home.html')

question_total = []
def quiz(request):
    
    obj=Question.objects.all()
    question_count = obj.count()*5
    question_total.append(question_count)
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1 
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)           
    return render(request, 'quiz.html',{'obj':obj,'questions':questions})



lst = []
anslist = []
answers = Question.objects.all()

for i in answers:
    anslist.append(i.answer)



def result(request):
    score = 0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score += 1*5
    return render(request,'result.html',{"score":score,'question_total':question_total[0]})


def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)