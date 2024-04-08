from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def receipes(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        print(receipe_name)
        print(receipe_description)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect("/receipes/")
    
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    
    context = {"receipes": queryset}
    return render(request, "receipes.html", context)

def delete_receipe(request, id):
    query = Receipe.objects.get(id=id)
    query.delete()
    return redirect("/receipes/")

def update_receipe(request, id):
    query = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        query.receipe_name = receipe_name
        query.receipe_description = receipe_description

        if receipe_image:
            query.receipe_image = receipe_image
        
        query.save()
        return redirect("/receipes/")

    
    context = {"receipes": query}
    return render(request, 'update_receipe.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')



    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
            
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created succesfully")

        return redirect('/register/')


    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
