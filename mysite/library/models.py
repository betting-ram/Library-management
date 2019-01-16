from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date




# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=80)
    cover = models.TextField(max_length=100000, blank=True, null=True)
    description = models.TextField(max_length=25000, blank=True, null=True)
    available = models.IntegerField(default=0)

    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("library:book_detail", kwargs={"id": self.id})



   # def __str__(self):
   #    return  self.borrower
   # @property
   # def is_overdue(self):
   #     if self.due_back and date.today() > self.due_back:
   #         return True
   #     return False
class Student(models.Model):
   # student_id = models.CharField(max_length=100,unique=True,null=True)
    firstname = models.CharField(max_length=100, default="", )
    lastname = models.CharField(max_length=100, default="", )
    department = models.CharField(max_length=100, default="", )
    section = models.CharField(max_length=50, default="")
    year = models.IntegerField()
    picture = models.ImageField(upload_to='pictures/',blank=True)

    def __str__(self):
        return self.firstname +' ' +self.lastname


class Borrow(models.Model):
    book = models.ManyToManyField(Book)
    student = models.ManyToManyField(Student)
    qty = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=25)

    def __str__(self):
        return str(self.book)