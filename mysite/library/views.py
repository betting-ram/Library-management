from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from .models import Book,Student,Borrow
from django.views.generic import ListView ,CreateView,DetailView, DeleteView, UpdateView
from .forms import Studentform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import UserCreationForm


# Create your views here.
def home(request):
   return render(request,"library/index.html")
#for contact
def contact(request):
   return render(request,"library/contact.html")
#for about us
def about(request):
   return render(request,"library/about.html")
#def admin(request):
#    return render(request,"library/base2.html")
#view the book

# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/login/')
def booklist(request):
    if  request.user.is_superuser:
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request, 'library/book_list.html',context)
    else:
        return HttpResponseRedirect("/login/")

 #class booklistview(LoginRequiredMixin,ListView):
 #  template_name = 'library/book_list.html'
 #   queryset = Book.objects.all()
  #  login_url = "/std/login"
  #  redirect_field_name = "hollaback"
  #  raise_exception = True


#detail view
def bookdetails(request,id=None):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request,'library/book_detail.html',context)


#  class bookdetailview(DetailView):
#     template_name = 'library/book_detail.html'
#    def get_object(self):
#        id_ = self.kwargs.get("id")
#        return get_object_or_404(Book, id=id_)


#add a book

class AddView(CreateView):

    template_name = 'library/book_add.html'
   # form_class = BookForm
    queryset = Book.objects.all()
    fields = ['title','book_type','author','language']

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



#update book
class updateView(UpdateView):
     template_name = 'library/book_add.html'
    # form_class = BookForm
     fields = ['title', 'book_type', 'author', 'language']
    # queryset= Book.objects.all()

     def get_object(self):
         id_ = self.kwargs.get("id")
         return get_object_or_404(Book, id=id_)


class deleteView(DeleteView):
    template_name = 'library/book_delete.html'
    # form_class = BookForm
    fields = ['title', 'book_type', 'author', 'language']
    success_url = reverse_lazy('library:book_list')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

#for std login


def stdlogin(request):

    if request.method == "POST":

        student_id = request.POST.get('student_id')
        firstname = request.POST.get('firstname')
        student = authenticate(request,student_id=student_id, firstname=firstname)
        if student is not None:
            login(request, student)
            return redirect("library:bookavailable")
    return render(request, "library/stdform.html")
   # else:
   #     context =  "invalid username or password"
   #     return render(request,'library/stdform.html',{context:'context'})




#for student registration



def studentsdetails(request):
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, 'student/std_form.html',context)
       # students = Student.objects.all()
       # return render(request, 'student/std_form.html', {"students": students})

#for adding std
def studentadd(request):
   # saved = False
   # my_form = Studentform
    if request.method == "POST":
        studentform = Studentform(request.POST,request.FILES)
        if studentform.is_valid():
              student = Student()
#              student.student_id = studentform.cleaned_data["student_id"]
              student.firstname = studentform.cleaned_data["firstname"]
              student.lastname = studentform.cleaned_data["lastname"]
              student.department = studentform.cleaned_data["department"]
              student.year = studentform.cleaned_data["year"]
              student.picture = studentform.cleaned_data["picture"]
              student.save()
              return redirect('/students/')
      #  sid = request.POST["student_id"]
      #  firstname = request.POST["firstname"]
      #  lastname = request.POST["lastname"]
      #  department = request.POST["department"]
       # year = request.POST["year"]
       # profile = request.POST.get("profile",False)
       # student = Student(student_id=sid, firstname=firstname, lastname=lastname, department=department, year=year,profile=profile)
       # student.save()
       # return redirect(reverse('library:students'))
    else:
        form = Studentform
        return render(request, 'student/signup_form.html',{'form':form})


#for additional view


#for additional purposes

#for borrowing books
def borrow(request):
    if request.method == "POST":
        student_id = request.POST['student_id']
        student = Student.objects.get(id=student_id)
        status = "Borrowed"
        books_id = request.POST.getlist('selector')
        for book_id in books_id:
            book = Book.objects.get(id=book_id)
            b = Borrow(qty=1, status=status)
            b.save()
            b.student.add(student)
            b.book.add(book)
            return redirect("library:borrow")
    students = Student.objects.all()
    books = Book.objects.all()
    datas = []
    for book in books:
        left = Borrow.objects.filter(status="Borrowed", book__title=book.title).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = -1
        else:
            l = int(left['qty__sum'])
        datas.append(book.available - l)
    return render(request, "student/borrow.html", {"datas": zip(books, datas), "students": students})

#to return book

def returning(request):
    if request.method == "POST":
        b_id = int(request.POST["borrow_id"])
        borrow = Borrow.objects.get(id=b_id)
        borrow.date = datetime.now()
        borrow.status = "Returned"
        borrow.save()
        return redirect('library:returning')
    borrows = Borrow.objects.all()
    return render(request, "student/return.html", {"borrows": borrows})

#for std update
class updatestdView(UpdateView):
    template_name = 'student/student_update.html'
    # form_class = BookForm
    fields = ['firstname','lastname','department','year','picture']
    success_url = reverse_lazy('library:students')

    # queryset= Book.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, id=id_)



class deletestdView(DeleteView):
    template_name = 'student/std_delete.html'
    #fields = ['student_id','firstname','lastname','department','year','profile']
    success_url = reverse_lazy('library:students')


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, id=id_)



#def Bookavailable(request):
#    book = Book.objects.all()
 #   bookinstance = BookInstance.objects.all()
 #   context = {'book':book,bookinstance:'bookinstance'}
 #   return render(request,'student/bookinstance.html',context)


#for issue book
#class deleteView(DeleteView):
 #   template_name = 'student/book_issue.html'
    # form_class = BookForm
  #  fields = ['book_name', 'book_type', 'author', 'language']
   # success_url = reverse_lazy('library:bookavailable')

#    def get_object(self):
##        return get_object_or_404(Book, id=id_)

# for std list
#class stdlistview(ListView):
#    fields = ['book_name', 'book_type', 'author', 'language']
#    template_name = 'student/stdlist.html'
 #   queryset = Book.objects.all()
#class stddetailview(DetailView):
#    template_name = 'student/std_detail.html'

 #   def get_object(self):
 #       id_ = self.kwargs.get("id")
 #       return get_object_or_404(Book, id=id_)