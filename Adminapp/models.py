from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName = models.TextField(max_length=50, null=False, blank=False)
    Description = models.TextField(max_length=50, null=False, blank=False)
    Category_Image = models.ImageField(upload_to="Category/")
    def __str__(self):
        return self.CategoryName
class EventDb(models.Model):
    Category_Name = models.TextField(max_length=50, null=False, blank=False)
    EventName = models.TextField(max_length=50, null=False, blank=False)
    Location = models.TextField(max_length=50, null=False, blank=False)
    Price=models.IntegerField(null=False, blank=False)
    Description = models.TextField(max_length=50, null=False, blank=False)
    Image = models.ImageField(upload_to = 'events/')
    def __str__(self):
        return self.EventName