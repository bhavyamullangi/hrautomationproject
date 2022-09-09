from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.views import View
from hrAutomation_candidate.models import applicant_data_table
from .models import hr_hradmin_data_table


# Create your views here.
def register(request):
    return render(request, 'hr_register.html', )


def hr_register(request):
    # to save hr data to database
    if request.method == 'POST':
        user_values = hr_hradmin_data_table()
        user_values.hrName = request.POST.get('hr_name')
        user_values.email = request.POST.get('email-id')
        user_values.password = request.POST.get('password')
        user_values.confirm_password = request.POST.get('confirm-password')

        if user_values.password == user_values.confirm_password:
            email_verify = hr_hradmin_data_table.objects.filter(email=user_values.email)
            print(email_verify)

            if email_verify.exists():
                messages.info(request, 'email is already exists')
                return redirect('hr_register')
            else:
                user_values.save()
                return redirect('hr_login')
        else:
            messages.info(request, 'password not matching')
            return redirect('hr_register')
    else:
        return render(request, 'hr_register.html', )


def hr_login(request):
    if request.method == 'POST':
        hr_id = request.POST.get('email-id')  # web entered id
        hr_password = request.POST.get('password')  # web entered password
        userpassword = hr_hradmin_data_table.objects.get(email=hr_id).password  # check password with database

        if userpassword == hr_password:
         return redirect('hr_search')

        else:
            messages.warning(request, 'in-correct password')
    else:
        return render(request, 'hr_login.html', )


def hr_search(request):

    candidates = applicant_data_table.objects.all()
    return render(request, 'hr_search.html', {'candidates': candidates})
