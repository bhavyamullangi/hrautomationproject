from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from .forms import ResumeForm,Applicant_loginFrom
from .models import applicant_data_table

# Create your views here.

class homeview(View):
  def get(self,request):
     form=ResumeForm()
     return render(request,'applicant_register.html',{'form':form})

  def post(self,request):
      form = ResumeForm(request.POST, request.FILES)
      entered_email = request.POST.get('email')
      email_verify = applicant_data_table.objects.filter(email=entered_email)

      if email_verify.exists():
        messages.info(request,'email is already exists')
        return render(request,'applicant_register.html',{'form':form})
        # return HttpResponse('email already exists')

      else:

       if form.is_valid():
        form.save()
        return render(request, 'applicant_home.html', {'form': form})
def applicant_login(request):
     if request.method=='POST':
         password=request.POST.get('password')  # web entered password
         form=Applicant_loginFrom(request.POST)
         if form.is_valid():
             cd=form.cleaned_data
             userpassword=applicant_data_table.objects.get(email=cd['email']).password
             if userpassword == password:

              return render(request, 'applicant_home.html')
             else:
                 messages.warning(request, 'in-correct password')

         else:
            return render(request, 'applicant_login.html')
     else:
      form=Applicant_loginFrom()
     return render(request, 'applicant_login.html',{'form': form})


class applicant_info(View):
    def get(self,request,pk):
     candidate=applicant_data_table.objects.get(pk=pk)
     return render(request,'applicant-info.html',{'candidate':candidate})


def applicant_home(request):

     return render(request, 'applicant_home.html',)

