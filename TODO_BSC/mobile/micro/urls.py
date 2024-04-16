from django.urls import path
from . import views

urlpatterns = [
    path('anil/',views.anil,name='anil'),
    path('signup/',views.signup,name='signup'),
    path('',views.signin,name='signin'),
    path('search/',views.search,name='search'),
    path('display/',views.display,name='display'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('signout/',views.signout,name='signout'),
    path('logo/',views.logo,name='logo'),
    path('finish/<int:id>',views.finish,name='finish'),
 
]
