from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from basicinventory.forms.auth import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.data)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            if not user:
                messages.warning(
                    request,
                    'Either email or password is invalid'
                )
            login(request, user)
            redirect_url = request.POST.get('next', None)
            if redirect_url:
                return redirect(redirect_url)
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid input while submitting the form')
            return redirect('login')
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')
