from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        return redirect("/")


class SignupView(generic.View):
    form_class = UserCreationForm
    redirect_url = "/"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = self.form_class()
        context = {
            "form": form
        }
        return render(request, "registration/signup.html", context)

    def post(self, request):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = self.form_class(self.request.POST)
        if form.is_bound and form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return redirect(self.redirect_url)

        else:
            password1 = self.request.POST.get("password1")
            password2 = self.request.POST.get("password2")
            username = self.request.POST.get("username")

            if password1 != password2:
                message = "Passwords did not match"
                form = self.form_class(self.request.POST)
                context = {
                    "form": form,
                    "message": message,
                }
                return render(self.request, "registration/signup.html", context)

            elif User.objects.filter(username=username).exists():
                message = "Username already taken"
                form = self.form_class(self.request.POST)
                context = {
                    "form": form,
                    "message": message,
                }
                return render(self.request, "registration/signup.html", context)


class LoginView(generic.View):
    redirect_url = "/"
    form_class = AuthenticationForm

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_url)

        form = self.form_class()
        context = {
            "form": form
        }
        return render(self.request, "registration/login.html", context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.redirect_url)

        else:
            message = "Incorrect username or password"
            form = self.form_class(self.request.POST)
            context = {
                "form": form,
                "message": message
            }
            return render(self.request, "registration/login.html", context)
