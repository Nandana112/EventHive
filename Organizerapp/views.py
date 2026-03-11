from django.shortcuts import render,redirect
from Adminapp.models import *
from Organizerapp.models import ContactDb,Registration,BookingDb
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date


# Create your views here.
def Home(request):
    categories = CategoryDb.objects.all()
    return render(request, 'Home.html', {'categories': categories})
def About(request):
    return render(request, 'About.html')
def Contact(request):
    return render(request, 'Contact.html')
def All_Events(request):
    events = EventDb.objects.all()
    return render(request, 'All_Events.html', {'events': events})
def Booking_details(request,):
    return render(request, 'Booking_Details.html')
def event_single(request, event_id):

    single_event = EventDb.objects.get(id=event_id)
    return render(request, 'event_single.html', {'single_event':single_event})
def save_contact(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Subject = request.POST.get("Subject")
        Message = request.POST.get("Message")
        obj=ContactDb(Name=Name, Email=Email, Subject=Subject, Message=Message)
        obj.save()
        return render(request, 'Contact.html')
def filter_events(request,eve_name):
    filter_events = EventDb.objects.filter(Category_Name=eve_name)
    return render(request, 'filter_events.html', {'filter_events': filter_events})


def sign_up(request):
    return render(request, 'sign_up.html')
def sign_in(request):
    return render(request, 'sign_in.html')
def save_registration(request):
    if request.method=='POST':
        uname=request.POST.get('Username')
        email = request.POST.get('Email')
        password=request.POST.get('Password')
        confirm_password=request.POST.get('Confirm_password')
        obj=Registration(Username=uname,Email=email,password=password,confirm_password=confirm_password)
        if Registration.objects.filter(Username=uname,password=password).exists():
            print("Username already exists")
            return redirect('sign_up')
        elif Registration.objects.filter(Email=email).exists():
            print("Email already exists")
            return redirect('sign_up')
        else:
            obj.save()
            return redirect('sign_in')
def user_logout(request):
    del request.session['Username']
    del request.session['password']
    return redirect('Home')
def user_login(request):
    if request.method == "POST":
        uname=request.POST.get('Username')
        password=request.POST.get('Password')
        if Registration.objects.filter(Username=uname,password=password).exists():
            request.session['Username'] = uname
            request.session['password'] = password
            return redirect('Home')
        else:
            return redirect('sign_in')
    else:
        return redirect('sign_in')
def save_booking(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Date = request.POST.get("Date")
        Category_Name = request.POST.get("Category_Name")
        EventName = request.POST.get("EventName")
        Location = request.POST.get("Location")
        Phone = request.POST.get("Phone")
        Price = request.POST.get("Price")
        Address = request.POST.get("Address")
        Message = request.POST.get("Message")

        if BookingDb.objects.filter(Date=Date).exists():
           messages.warning(request,"This date is already booked!")
           return render(request, 'Home.html')

        else:
          BookingDb.objects.create(Name=Name,Email=Email,Date=Date,Category_Name=Category_Name,EventName=EventName,Location=Location,
                                     Phone=Phone,Price=Price,Address=Address,Message=Message)

          send_mail('Event booking Conformation','hello{Name},your {EventName} Booking on {Date} is received',settings.EMAIL_HOST_USER,[Email],fail_silently=False,)
          messages.success(request, 'booked successfully')
        return render(request, 'Home.html', {'messages':messages})
