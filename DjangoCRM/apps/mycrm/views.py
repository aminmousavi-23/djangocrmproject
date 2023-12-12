from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Login Function
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have login successfully.')
            return redirect('home')
        else:
            messages.success(request, 'There is no account with that username!!!')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})
    
    return render(request, 'home.html')

# Logout Function

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout successfuly.')
    return redirect('home')

# Register Function
def Register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been register successfuly.')
            return redirect('home')
        elif password1 != password2:
            messages.success(request, 'Your password and confirm password are not same!!!')
            return redirect('Register')
    else:
        form = SignUpForm()
        return render(request, 'Register.html', {'form':form})
    return render(request, 'Register.html')

# Customer Records
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You have to login to see the data!!!')
        return redirect('home')