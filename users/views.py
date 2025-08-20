from django.db.models import Q
from django.db.models.sql import AND
from django.shortcuts import render
from .models import Userregistration
from .forms import UserRegForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def login_page(request):
    context = {'message': 'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Userregistration.objects.filter(Q(username=username), Q(password=password))
        if data:
            return render(request, 'core/index.html')
        else:
            return render(request, 'users/login_page.html', context)
    return render(request, 'users/login_page.html')


def register(request):
    form = UserRegForm(request.POST)
    if request.method == "POST":

        print('inside post')
        if form.is_valid():
            form.save()
            return render(request, 'core/index.html')
    # else:
    #     form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')  # Redirect to your desired page after logout
