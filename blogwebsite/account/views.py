from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request,"account/login.html",
                          {"error": "email or password is wrong"})
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html",{"error":"Username already exists"})
            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html",{"error":"Email already exists"})
            else:
                user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                user.save()
                return redirect("login")
        else:
            return render(request, "account/register.html",{"error":"Password does't match"})



    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
