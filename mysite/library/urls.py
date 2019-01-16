
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import  AddView,updateView,deleteView,updatestdView,deletestdView
from django.contrib.auth.views import LoginView

app_name = 'library'

urlpatterns = [
       #for home
       path('',views.home,name = 'home'),
       #for contact
       path('contact/',views.contact,name ='contact' ),
       #for about us
       path('about/',views.about,name='about'),

       # for view book
       path('book/list/',views.booklist,name='book_list'),
       # path('book/list/',booklistview.as_view(),name = 'book_list'),
       #for detail view
       path('detail/<int:id>/', views.bookdetails, name='book_detail'),
       # path('detail/<int:id>/',bookdetailview.as_view(),name='book-detail'),
       # add a new book
       path('add/book/',AddView.as_view(),name ='bookadd' ),
       #update book
       path('update/<int:id>/',updateView.as_view(), name='bookupdate'),
       #delete book
       path('delete/<int:id>/', deleteView.as_view(), name='bookdelete'),
       #for student registration
#       path('std/registration/', views.students, name="students"),
       #for student login
        path('std/login/', views.stdlogin, name='stdlogin'),
       #for std details
       path('students/', views.studentsdetails, name="students"),
       #add std
       path('students/add/', views.studentadd, name='std_add'),

       #for borrows books
       path('borrow/', views.borrow, name="borrow"),

       #to return book
       path('return/',views.returning,name='returning'),
       # update student
       path('update/std/<int:id>/', updatestdView.as_view(), name='studentupdate'),
       # delete book
       path('delete/std/<int:id>/', deletestdView.as_view(), name='studentdelete'),
       #for addditional purpose
      # path('user/login/', views.login, name="user"),
      # path('signup/user/', views.register, name='signup_user'),
      # path('logout/', views.logout, name='logout'),

       #for available books to students
#      path('available/books/',views.Bookavailable,name='bookavailable'),
       #for issue book
#       path('issue/<int:id>/', deleteView.as_view(), name='issue'),
       # for std details
#       path('std/list/',stdlistview.as_view(), name='stdlist'),
       # for std details
#       path('std/detail/<int:id>/',stddetailview.as_view(),name='stddetails'),
]
