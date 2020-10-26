from django.shortcuts import render, HttpResponse, redirect
from .models import User
from app1.views import index  
from .decorators import my_login_required
from .models import LoginDetails, User
from django.contrib.auth.hashers import make_password, check_password


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        location = request.POST['location']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        client_ip = request.META['REMOTE_ADDR']
        if password1 == password2:
            hash = make_password(password1)
            User.objects.create(username=username, email=email,
                                groupid=location, ipaddress=client_ip, password=hash)
            return redirect(login)
        else:
            return HttpResponse("Mismatch")
    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        if request.session.get('user', False):
            user = request.session.get('user')
            return redirect(index)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.get(username=username)
            hashed = user_obj.password
            user = check_password(password, hashed)
            ld = LoginDetails(userid= user_obj, 
                            created_on=user_obj.created_on, 
                            ipaddress= request.META['REMOTE_ADDR'],
                            useragent=request.META['HTTP_USER_AGENT'],
                            )
            ld.save()
            if user:
                request.session['user'] = username
                return redirect(index)
            else:
                return HttpResponse("Enter valid details")
    return render(request, 'users/login.html')


@my_login_required
def logout(request):
    try:
        del request.session['user']
        return redirect(login)
    except KeyError:
        return redirect(login)
