from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    """the main function for the registration, if form is valid return the login page"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/compte/connection/login')
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "account/register.html", context)
