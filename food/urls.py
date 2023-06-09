from django.urls import path
from . import views

urlpatterns = [ 
    path('food/',views.food,name='food'),
    path('menu/',views.menu,name='menu'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/', views.cart,name='cart'),
    path('details/<int:id>',views.details,name='details'),
    path('check_out/',views.check_out,name='check_out'),
    path('place_order/',views.place_order,name="place_order"),
    path('orders/',views.orders,name="orders"),
    path('search/',views.search,name="search"),
    path('delete_cart_item/<str:id>',views.delete_cart_item,name="delete_cart_item")
]