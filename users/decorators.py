from django.shortcuts import redirect


def my_login_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.session.get('user')
        if user:
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper
