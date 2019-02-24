from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":#if any value is is given by user
        if request.POST['password1'] == request.POST['password2']:#when password and confirming password is equal
            try:
                user=User.objects.get(username=request.POST['username'])#when username is already present
                return render(request, 'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])#if username is unique and both the password are same it stores the data
                auth.login(request,user)#for logging user in
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'password must match'})#if password and confirming password misses matched        
    else:
        return render(request, 'accounts/signup.html')#if fields are empty and user clicks signup
    

def login(request):
    if request.method=='POST':#if any value is is given by user
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')
    #to do need to route to home page
    #and dont forget to logout
        

    
    
    
    

