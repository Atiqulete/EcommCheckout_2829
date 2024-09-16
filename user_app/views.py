# Create your register page here.
from django.shortcuts import render, redirect, HttpResponse
from user_app.forms import RegisterForm,UserUpdate,ProfileUpdate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages

# Create your register code here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form=RegisterForm()
    return render(request,'user_app/register.html',{'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            context = {
               'error_message' : 'username or password is incorrect!!!',
            }
        return render(request,'user_app/login.html',context)
    return render(request, 'user_app/login.html')

# Create your logout code here.
def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request,'user_app/profile.html')

def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST,instance=request.user)
        p_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request,'Profile details updated.')
            return redirect('profile')
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request,'user_app/profileupdate.html',context)

