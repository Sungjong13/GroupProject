from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, View
from .models import User
from .forms import CreateAccountForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "main.html"


def login(request):
    # 들어온 데이터 변수 저장
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # DB와 데이터 비교
        try:
            login_user = User.objects.get(email=email)
        except:
            messages.error(request, "회원정보를 찾을 수 없습니다.")
        login_user = authenticate(request, email=email, password=password)

        if login_user is not None:
            auth_login(request, login_user)
            return redirect("home")

        else:
            messages.error(request, "이메일 혹은 비멀번호가 틀렸습니다.")

    return render(request, "users/login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")


def create_account(request):
    # 인증이 안된 경우 회원가입 페이지 - url 타고 들어오는 경우 차단. 인증 된 사용자인 경우 홈으로.
    if not (request.user.is_authenticated):
        if request.method == "POST":
            form = CreateAccountForm(request.POST)
            print(form)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password"])
                user.save()

                login_user = authenticate(
                    username=form.cleaned_data["email"],
                    password=form.cleaned_data["password"],
                )
                # 회원가입 시 자동 로그인
                auth_login(request, login_user)
                return redirect("home")
        else:
            form = CreateAccountForm()

        return render(request, "users/account.html", {"form": form})
    else:
        return redirect("home")


def check_email(request):
    try:
        _email = User.objects.get(email=request.GET["name"])
    except Exception as e:
        _email = None
    print(_email)
    result = {
        "result": "success",
        "data": "not exist" if _email is None else "exist",
    }
    return JsonResponse(result)


def check_nickname(request):
    try:
        _nickname = User.objects.get(nickname=request.GET["name"])
    except Exception as e:
        _nickname = None
    result = {
        "result": "success",
        "data": "not exist" if _nickname is None else "exist",
    }
    return JsonResponse(result)
