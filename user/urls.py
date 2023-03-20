from django.urls import path
from . import views
urlpatterns = [   
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('thankYou/',views.thankYou,name='thankYou')
]
 