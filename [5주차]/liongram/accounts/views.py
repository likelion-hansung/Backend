from django.shortcuts import redirect, render
from .forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    #  GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = { 'form' : form }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')

def login_view(request):
    if request.method =='GET':
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            # 응답
            return redirect('index')
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            return render(request, 'accounts/login.html', {'form' : form})
        
def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        # 비즈니즈 로직 처리
        logout(request)
    # 응답
    return redirect('index')