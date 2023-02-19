from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        if get_password != get_confirm_password: # checking if password the user inserted are the same
            messages.info(request,'Password is not matching...')
            return redirect('/auth/signup/')

        try: # Checking if the email already exists
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User is created. Please login.')
        return redirect('/auth/login/')

    return render(request,'signup.html')

@csrf_exempt
def handleLogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login success")
            return redirect('/')
        else:
            messages.error(request, "Wrong username or password")

    return render(request,'login.html')

def handleLogout(request):
    return render(request,'login.html')