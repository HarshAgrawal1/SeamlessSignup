from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from home.models import Registration
from django.contrib.auth.models import User,auth
from django.contrib import messages
from aidiet import settings
import requests
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    # return HttpResponse("This is home page")
    return render(request,'signup.html')


# def login(request):
#     if request.method=="POST":
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']


#         Registratio=Registration(first_name=first_name,last_name=last_name,email=email,password=password)
#         Registratio.save()
#         return render(request,'login.html')
#     return render(request,'login.html')

def login(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the email already exists in the database
        if Registration.objects.filter(email=email).exists():
            # Email already exists, do not save and return an error or simply return nothing
            
            return render(request, 'login.html', {'error': 'Email already exists'})
        else:
            # Email does not exist, save the new record
            new_registration = Registration(first_name=first_name, last_name=last_name, email=email, password=password)
            new_registration.save()
            send_mail(
                    subject='Login Successful',
                    message=f'',
                    from_email='agrawalharsh0522@gmail.com',  # Use the email you set in settings.py
                    recipient_list=[email],
                    fail_silently=False,
            )
            return render(request,'login.html')
            
    return render(request,'login.html')

def send_login_email(user_email):
    subject = 'Login Notification'
    message = 'You have successfully logged in.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)

def process_login(request):
    if request.method=="POST":
        check_email=request.POST['email']
        check_password=request.POST['password']

        try:
            user = Registration.objects.get(email=check_email)
            if user.password == check_password:
                # Login successful, send an email to the user
                # send_mail(
                #     subject='Login Successful',
                #     message=f'Hello You have successfully logged in.',
                #     from_email='agrawalharsh0522@gmail.com',  # Use the email you set in settings.py
                #     recipient_list=[check_email],
                #     fail_silently=False,
                # )
                return redirect("/home")
            else:
                messages.error(request, 'Incorrect Password!!')
                return redirect('/login')
                # return render(request,'login.html',{'error':'INcorrect Password!!'})


        # Problem faced in this code urls not matching  ---- DONE
        except Registration.DoesNotExist:
            messages.error(request, 'Email not exist, PLease Create an account first!!')
            # return redirect('/')
            # return messages.error(request,'Email not exist')
    
    return render(request,'login.html')

        
def home(request):
    # username = request.session.get('first_name')
    # email = request.session.get('email')
    # context = {
    #     'username': username,
    #     'email': email,
    # } 

    return render(request,'home.html')


