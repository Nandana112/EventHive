from django.db import models
from django.db.models import Model


# Create your models here.
class Registration(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    confirm_password = models.CharField(max_length=50,null=True,blank=True)


class ContactDb(models.Model):
 Name=models.TextField(max_length=50, null=False, blank=False)
 Email=models.EmailField(max_length=50, null=False, blank=False)
 Subject=models.TextField(max_length=50, null=False, blank=False)
 Message=models.TextField(max_length=50, null=False, blank=False)

class BookingDb(models.Model):
 Name=models.CharField(max_length=50, null=False, blank=False)
 Email=models.EmailField(max_length=50, null=False, blank=False)
 Date=models.DateField(null=False, blank=False,unique=True)
 Category_Name=models.TextField(max_length=50, null=False, blank=False)
 EventName=models.TextField(max_length=50, null=False, blank=False)
 Location=models.TextField(max_length=50, null=False, blank=False)
 Phone = models.CharField(max_length=50, null=False, blank=False)
 Price=models.IntegerField( null=False, blank=False)
 Address=models.TextField(max_length=50, null=False, blank=False)
 Message=models.TextField(max_length=50, null=False, blank=False)

 status=models.TextField(max_length=50,choices=[('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')],
                         default='Pending')
 payment_status = models.TextField(
        choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')],
        default='Unpaid'
    )
 def __str__(self):
     return self.Name
class ReviewDb(models.Model):
    Name=models.CharField(max_length=50, null=False, blank=False)
    event_type= models.CharField(max_length=10, null=False, blank=False)
    rating=models.IntegerField(null=False, blank=False)
    comment=models.TextField(max_length=50, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email