from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomCreationForm, CustomChangeForm

def login(request):
    # 로그인도 세션을 create하는 과정이다
    if request.method == 'POST':
        # print(f'next={request.POST}')
        # next 인자 받아온 거 조회해보기 post


        # form = AuthenticationForm(request, data = request.POST)
        # 폼태그는 인자 순서가 정해져있음 두번째는 무조건 데이터
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 (세션 데이터 생성) 진행
            auth_login(request, form.get_user())
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    # if request.method == 'POST':
    #     form = CustomCreationForm(request.POST)
    #     if form.is_valid():
    #         # form.save()
    #         # 1. DB에 user 저장
    #         # 2. 내가 현재 저장하고자하는 객체를 반환
    #         user = form.save()
    #         # 회원가입 하자마자 로그인
    #         auth_login(request, user)
    #         return redirect('articles:index')
    # else:
    #     form = CustomCreationForm()
    # context = {
    #     'form' : form,
    # }
    # return redirect(request, 'accounts/signup.html', context)
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)