from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    if request.method =="GET":
        return render(request, template_name="user_app/login.html")
    elif request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if next is not None:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect("/buk/buk")
        5/0
