from django.shortcuts import redirect


def user_not_authenticated(function=None, redirect_url='home'):

    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            
            return view_func(request, *args, **kwargs)
        return wrapped_func
    
    if function:
        return decorator(function)
    return decorator