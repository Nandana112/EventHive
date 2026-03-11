from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Adminapp.models import *
from django.contrib import messages
from Organizerapp.models import *

from Organizerapp.models import ContactDb


# Create your views here.
def Dashboard(request):
    return render(request, 'Dashboard.html')
def Events(request):
    categories=CategoryDb.objects.all()
    return render(request, 'All_Events.html',{'categories':categories})
def View_Event(request):
    data=EventDb.objects.all()
    return render(request, 'View_Event.html',{'data':data})
def Event_Category(request):
    return render(request, 'Event_Category.html')
def View_Category(request):
    categories=CategoryDb.objects.all()
    return render(request, 'View_Category.html',{'categories':categories})
def Admin_Loginpage(request):
    return render(request,'admin_login.html')
def Admin_Login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pword)
            if user is not None:
                login(request,user)
                request.session['username'] = uname
                request.session['password'] = pword
                messages.success(request,'Login Successful')
                return redirect('Dashboard')
            else:
                print("invalid details....")
                return redirect('Admin_Loginpage')
        else:
            print("user not found....")
            messages.error(request,'Username or Password is incorrect')
            return redirect('Admin_Loginpage')


def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,'Logout Successful')
    return redirect('Admin_Loginpage')
def save_event(request):
        if request.method == "POST":
            Category_Name=request.POST.get('Category_Name')
            EventName=request.POST.get('EventName')
            Location=request.POST.get('Location')
            Price=request.POST.get('Price')
            Description = request.POST.get('Description')
            Image = request.FILES['Image']
            EventDb.objects.create(Category_Name=Category_Name,EventName=EventName,Location=Location,Price=Price, Description=Description, Image=Image)
            messages.success(request,'Event Created')
            return redirect('Events')
def save_category(request):
    if request.method == "POST":
        CategoryName=request.POST.get('CategoryName')
        Description = request.POST.get('Description')
        Category_Image = request.FILES['Category_Image']
        CategoryDb.objects.create(CategoryName=CategoryName, Description=Description,Category_Image=Category_Image)
        messages.success(request,'Category Created')
        return redirect('Event_Category')
def delete_category(request, cat_id):
    category = CategoryDb.objects.filter(id=cat_id)
    category.delete()
    messages.success(request, 'category Deleted successfully')
    return redirect(View_Category)

def edit_category(request, cat_id):
    category = CategoryDb.objects.get(id=cat_id)
    return render(request, 'Edit_Category.html',{'category':category})
def update_category(request, cat_id):
    category=CategoryDb.objects.get(id=cat_id)
    if request.method == "POST":
           category.CategoryName = request.POST.get('CategoryName')

           category.Description = request.POST.get('Description')

           if'Category_Image' in request.FILES:
               category.Category_Image = request.FILES['Category_Image']

           category.save()
           messages.success(request, 'category updated successfully')
           return redirect('View_Category')



def delete_event(request, bk_id):
    data = EventDb.objects.filter(id=bk_id)
    data.delete()
    messages.success(request, 'Event Deleted successfully')
    return redirect(View_Event)

def edit_event(request, bk_id):
    data = EventDb.objects.get(id=bk_id)
    categories=CategoryDb.objects.all()
    return render(request, 'Edit_events.html',{'data':data, 'categories':categories})


def update_event(request, bk_id):
    data=EventDb.objects.get(id=bk_id)
    if request.method == "POST":
           data.Category_Name = request.POST.get('Category_Name')
           data.EventName = request.POST.get('EventName')
           data.Location = request.POST.get('Location')
           data.Description = request.POST.get('Description')

           if'Image' in request.FILES:
               data.Image = request.FILES['Image']

           data.save()
           messages.success(request, 'Event updated successfully')
           return redirect('View_Event')

def Contact_details(request):
    contact=ContactDb.objects.all()
    return render(request, 'Contact_details.html',{'contact':contact})
def delete_contact(request, con_id):
    contact = ContactDb.objects.filter(id=con_id)
    contact.delete()
    messages.success(request, 'contact Deleted successfully')
    return redirect(View_Category)