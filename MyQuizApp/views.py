from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from MyQuizApp.forms import *
from MyQuizApp.models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from taggit.models import Tag
from  django.views.generic import ListView

from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
           #print(request.post)
           questions=QuestionsModel.objects.all()
           score=0
           wrong=0
           correct=0
           total=0
           for i in questions:
                 total=total+1
                 print(request.POST.get(i.question))
                 print(i.answer)
                 #print()

                 if i.answer== request.POST.get(i.question):
                        score=score+10
                        correct=correct+1
                 else:
                        wrong=wrong+1

           percentage=score/(total*10) *100
           context={
                        'score' : score,
                        'correct' : correct,
                        'wrong' : wrong,
                        'percentage' : percentage,
                        'total' : total,
                        'time' : request.POST.get('timer'),
           }
           return render(request,'MyQuizApp/result.html',context)
    else:
        questions=QuestionsModel.objects.all()
        context ={
            'questions':questions
        }
        return render(request,'MyQuizApp/home.html',context)



def addQuestion(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if (request.method == 'POST'):
            form = AddQuestionForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'MyQuizApp/AddQuestions.html', context)
    else:
        return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = userform()
        if request.method == 'POST':
            form = userform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'MyQuizApp/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'MyQuizApp/login.html', context)


def logoutPage(request):
    request.session.clear()
    return render(request, 'MyQuizApp/logout.html')


def homepageview(request):
    return render(request, 'MyQuizApp/frontpage.html')


from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    posts = QuestionsModel.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'MyQuizApp/home.html', context)

