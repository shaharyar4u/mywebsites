from django.shortcuts import render, HttpResponse
#from django.http import HttpResponseRedirect
from datetime import datetime
from home.models import Contact
from home.models import Registration
from django.contrib import messages
from home import views
#from django.conf import settings
#from .forms import EmailSignupForm
#from .models import signup
import requests
import pyrebase
#from marketing.forms import EmailSignupForm


'''
config={
    "apiKey": "AIzaSyCvXtcDeOBT9usvgM5UzI2CEqIK0m_IBb4",
    "authDomain": "shaharyar-s-website.firebaseapp.com",
    "databaseURL": "https://shaharyar-s-website-default-rtdb.firebaseio.com",
    "projectId": "shaharyar-s-website",
    "storageBucket": "shaharyar-s-website.appspot.com",
    "messagingSenderId": "86423165052",
    "appId": "1:86423165052:web:1387db470c3a6d116b11f9",
  }
        firebase=pyrebase.initialize_app(config)
        authe=firebase.auth()
        database=firebase.database()

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    }
    channel_name=database.child('Name').get().val()
    channel_department = database.child('dapartment').get().val()
    channel_designation = database.child('designation').get().val()
    return render(request, 'index.html', {
        "channel_name"=channel_name,
        "channel_designation" = channel_designation,
        "channel_department" = channel_department
    })
    # return HttpResponse("this is homepage")
'''
#Mailchimp Integration
'''MAILCHIMP_API_KEY=settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER=settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID=settings.MAILCHIMP_EMAIL_LIST_ID 

api_url=f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint=f'{api_url'}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data= {
        "email_address":email,
        "status":"subscribed"
    }
    r=request.post(
        members_endpoints
        auth=("", MAILCHIMP_API_KEY),
        data=json.dump(data)
    )
    return r.status_code,r.json()

def email_list_signup(request):
    form=EmailSignupForm(request.POST or None)
    if request.method== "POST":
        if form.is_valid():
            email_signup_qs=Signup.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request,"You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def base(request):
    featured=Post.objects.filter(featured=True)
    latest=Post.objects.order_by('=timestamp')[0:3] 
    form= EmailSignupForm()
    if request.method=="POST:
        email= request.POST["email"]
        new_signup= Signup()
        new_signup.email= email
        new_signup.save()
        )  

    context={
        'object_list':featured,
        'latest': latest
        'form': form
    }
    return render(request, 'base.html', context)'''   

def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def services(request):
    return render(request, 'services.html')

def research(request):
    return render(request, 'research.html')

def thought(request):
    return render(request, 'thought.html')

def blog(request):
    return render(request, 'blog.html')

def video(request):
    return render(request, 'video.html')

def desacademy(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        regd = Registration(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        regd.save()
        messages.success(request, 'Your registration is successful!')
    return render(request, 'desacademy.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

