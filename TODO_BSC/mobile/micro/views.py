from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.models import todo
from django.db.models import Q

# Create your views here.

def anil(request):
    d=todo.objects.all()
    return render(request,"index.html",{"table":d})
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        task=request.POST.get('task')
        due=request.POST.get('due')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=User.objects.create_user(username=username,password=password,email=email,)
            todo.objects.create(task=task,due=due,uid_id=user.id)
            messages.info(request,"succesfully register Logged Now")
            return redirect("signin")
        else:
            messages.info(request,"password do not match")
            return redirect("signup")
    return render(request,"signup.html")
def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"you are successfully logged!")
            return redirect("display")
        else:
            messages.info(request,"username or password id incorrect")
            return redirect("signin")
    return render(request,"signin.html")

def display(request):
    # d=todo.objects.filter(Q(status="Not started")|Q(status="In progress"),uid_id=request.user.id)
    d=todo.objects.all()
    return render(request,"index.html",{'table':d})
        


def search(request):
    if request.method=="POST":
        search=request.POST.get('search')
        task = todo.objects.filter(Q(task=search)|Q(status=search))
        print(task)
        print(request.user.username)
    return render(request,"index.html",{"table":task})

login_required(login_url="task")
def task(request):
    if request.method =="POST":
        task =request.POST.get("task")
        due =request.POST.get("due")
        user=todo.objects.filter(uid_id=request.user.id,task=task,due=due)
        if not user:
            todo .objects.create(task=task,due=due,uid_id=request.user.id)
            messages.info(request,"successfully add task")
            return redirect('display')
        else:
            messages.info(request,"task already exist enter a new task")
            return render(request,"index.html")
    return render(request,"index.html")

def due(request):
    if request.method =="POST":
        search= request.POST.get('search')
        task=todo.objects.filter(uid_id=request.user.id,due=search)
        print(task)
        return render(request,'index.html',{"table":task})
    return render(request,"index.html")

def delete(request,id):
    todo.objects.filter(id=id).delete()
    messages.info(request,'successfully delete')
    return redirect('display')
   
def edit(request,id):
    if request.method == "POST":
        task=request.POST.get('task')
        due=request.POST.get('due')
        todo.objects.filter(id=id).update(task=task,due=due)
        messages.info(request,'success update')
        return redirect('display')
    return render(request,'signup.html')
def signout(request):
    logout(request)
    messages.info(request,"YOU ARE SUCCESSFULLY LOGGED OUT")
    return redirect('signin')
def logo(request):
    return render(request,"home.html")
def finish(request,id):
    todo.objects.filter(id=id).update(status="complete")
    messages.info(request,"status change")
    return redirect('display')
