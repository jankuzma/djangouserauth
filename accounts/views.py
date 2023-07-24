from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from hello.views import hello


# Create your views here.
class loginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'hello.html')
        message = 'invalid user or password'
        return render(request, 'accounts/login.html', {'msg':message})

class LogoutView(View):
    def get (self, request):
        logout(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request,'accounts/register.html')
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')
        if password2 == password1:
            u = User(first_name=first_name, last_name=last_name, username=username)
            u.set_password(password1)
            u.save()
            login(request, u)
            return render(request, 'hello.html')