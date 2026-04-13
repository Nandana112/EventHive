from django.shortcuts import render,redirect
from Adminapp.models import *
from Organizerapp.models import ContactDb,Registration,BookingDb,ReviewDb,Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import json
import razorpay



# Create your views here.
def Home(request):
    reviews = ReviewDb.objects.all()
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)

    return render(request, 'Home.html', {'categories': categories, 'reviews': reviews})
def About(request):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    return render(request, 'About.html',{'categories':categories})
def Contact(request):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    return render(request, 'Contact.html',{'categories':categories})
def All_Events(request):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    events = EventDb.objects.all()
    return render(request, 'All_Events.html', {'events': events, 'categories':categories})
def Booking_data(request,):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    bookings = BookingDb.objects.filter(Name=request.session['Username'])

    payment = None

    if bookings.exists():
        users = bookings.last()
        amount = users.Price * 100  # Razorpay needs paisa

        client = razorpay.Client(auth=("rzp_test_ScV3BRoik1X3yH", "6a4svDrh3uU66w4VxGxAwtGA"))

        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1
        })

    return render(request, 'Booking_data.html',{'bookings': bookings,
                                                'categories':categories, 'payment':payment,'amount': amount if bookings.exists() else 0})
def event_single(request, event_id):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    single_event = EventDb.objects.get(id=event_id)
    booked_dates = BookingDb.objects.values_list('Date', flat=True)
    booked_dates = [d.strftime("%Y-%m-%d") for d in booked_dates]
    context = {
        'booked_dates':json.dumps(booked_dates),
        'single_event':single_event,
        'categories': categories,
    }

    return render(request, 'event_single.html',context)

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
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    filter_events = EventDb.objects.filter(Category_Name=eve_name)
    return render(request, 'filter_events.html', {'filter_events':filter_events,'categories':categories})


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
            messages.success(request, 'Registration successful')
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
           return redirect ('Home')

        else:
          booking=BookingDb.objects.create(Name=Name,Email=Email,Date=Date,Category_Name=Category_Name,EventName=EventName,Location=Location,
                                     Phone=Phone,Price=Price,Address=Address,Message=Message)

        message = f"""
        Hello {booking.Name},

        Your event booking has been confirmed.

        Event: {booking.EventName}
        Date: {booking.Date}
        payment: {booking.Price}
        Category: {booking.Category_Name}

        Thank you for choosing EventHive.

        Regards,
        EventHive Team
        """

        send_mail(
            'Event Booking Confirmation',
            message,
            settings.EMAIL_HOST_USER,
            [booking.Email],
            fail_silently=False
        )
        return render(request, 'Home.html', {'messages':messages})
def Review(request):
    categories = CategoryDb.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')

        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
    reviews=ReviewDb.objects.all()
    return render(request, 'Review.html',{'reviews':reviews,'categories':categories})
def save_review(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        event = request.POST.get('event')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        obj=ReviewDb(Name=Name,event_type=event,rating=rating,comment=comment)
        obj.save()
        return redirect(Review)
def remove_booking(request, book_id):
    bookings = BookingDb.objects.filter(id=book_id)
    bookings.delete()
    messages.success(request, 'Booking Removed successfully')
    return redirect(Booking_data)

