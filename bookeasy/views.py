from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import django
import uuid
# Create your views here.

# def home(request):
#     return HttpResponse("Hello World")

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import login
from .form import signup
from .form import payment
from .models import movie, movie_User, order, transactions
from django import forms

def get_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = movie_User.objects.get(role=1, django_user__email=email)
            except movie_User.DoesNotExist:
                # Handle user not found
                error_message="User does not exist"
                return render(request, 'log.html', {'form': form, 'error_message':error_message})

            if not user.django_user.check_password(password):
                # Handle incorrect password
                error_message="Incorrect password"
                return render(request, 'log.html', {'form': form, 'error_message':error_message})
                
            login(request, user.django_user)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = login()

    return render(request, 'log.html', {'form': form})

def get_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = signup(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            django_user = django.contrib.auth.get_user_model()(email=email, username=uuid.uuid4(), last_name=last_name, first_name=first_name)
            django_user.set_password(password)
            django_user.save()
            movie_User(django_user=django_user, role=1).save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = signup()

    return render(request, 'signup.html', {'form': form})

def get_index(request):
    return render(request, 'index.html')

def get_moviepage(request,movie_id):
    mov = get_object_or_404(movie, id=1)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = signup(request.POST)
        # check whether it's valid:
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            ord = order(quantity=int(quantity),movies=mov, discount=0)
            ord.total_amount = ord.quantity * mov.amount - ord.discount
            ord.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(f'/payment/{ord.id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = signup()
    return render(request, 'moviepage.html', {'form': form})

def get_payment(request, order_id):
    ord = get_object_or_404(order, id=order_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = payment(request.POST)
        # check whether it's valid:
        if form.is_valid():
            txn = transactions(order=ord, **form.cleaned_data)
            txn.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = payment()


    return render(request, 'payment.html', {'form': form, 'total_amount':ord.total_amount})

def get_cancellation(request):
    return render(request, 'cancellation.html')

def get_about(request):
    return render(request, 'about.html')
