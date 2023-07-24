from django.contrib.auth import authenticate, login
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
            return redirect('hello')
        message = 'invalid user or password'
        return render(request, 'accounts/login.html', {'msg':message})