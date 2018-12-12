from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django import forms
from django.contrib.auth import authenticate, login
from .models import userinfo
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.contrib import messages


'''testing purpose'''
#def home(request):
 #   print("hellow")
    #return render(request,"home/signup.html")
  #  return HttpResponse("<h2>hello</h2>")

'''signup form'''

def signup(request):

    '''if form is submitted'''

    if request.method == 'POST':
        #print("hello form is submitted")

        form = UserRegistrationForm(request.POST)

        '''checking whether form is valid or not'''

        if form.is_valid():

            '''checks whether the email contains '@' or not'''
            
            try:

                validate_email(form.cleaned_data["email"])
                valid_email = True
                #print("correct mail ")
            except :

                valid_email = False
                #print("wrong mail ")

            '''if it doesnot contain @ raises an error'''

            if valid_email == False:
                messages.warning(request, 'please enter the correct email.')  
                form = UserRegistrationForm()
                return render(request, 'home/signup.html', {'form' : form})
                #return HttpResponse("<h2>enter valid email address</h2>")
            '''if email contains '@' '''

            '''storing the data in table'''

            username=form.cleaned_data["username"]
            password=make_password(form.cleaned_data["password"])
            email=form.cleaned_data["email"]

        
            a=userinfo(username=username,password=password,email=email)

            '''saving the data in the table'''

            a.save()
            #print(a.username)

            '''rendering to a pages says user is registered'''

            return HttpResponse("<h2>the user is registered</h2>")

        else:

            ''' If form is not valid return the signup page again'''

            messages.warning(request, 'form is invalid please enter the correct data')  
            form = UserRegistrationForm()
            return render(request, 'home/signup.html', {'form' : form})
                
    else:   
        
        form = UserRegistrationForm()
        return render(request, 'home/signup.html', {'form' : form})


