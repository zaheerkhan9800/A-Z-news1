from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from eastnotes.form import LoginForm, RegForm


# Display login page and perform login operation
def login(request):
    # Here only the login operation, the verification part is completed in forms.py
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('blog:index')))  # Redirect to the previous page
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login/login.html', context)


# Display the registration page and perform registration operations
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']

            # registered user
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            template = render_to_string('login/email_template.html', {'name': reg_form.cleaned_data.get('username')})

            email = EmailMessage(
                "Thanks for signing up! Keep learning",
                template,
                settings.EMAIL_HOST_USER,
                [reg_form.cleaned_data.get('email')],

            )

            email.fail_silently = False,
            email.send()

            #Log in automatically after registration
            user = auth.authenticate(username=username,password=password)
            auth.login(request, user)

            # Jump to the page before entering the registration page
            return redirect(request.GET.get('from',reverse('blog:index')))  # Redirect to the previous page

    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'login/register.html', context)
