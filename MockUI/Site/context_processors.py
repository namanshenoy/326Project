def add_my_login_form(request):
    return {
        'login_form': LoginForm(),
    }