from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . models import Cuisine, Food, Order

# Create your views here.

def food(request):
    return HttpResponse("Came to Food")

def search(request):
    # result = Food.objects.filter(name__contains=val)
    # print(result)
    return HttpResponse(result)

def menu(request):
    foods = Food.objects.all()
    context = {
        'food' : foods
    }
    return render(request,'food/menu.html',context)

def details(request, id):
    food = Food.objects.get(id=id)
    context = {
        'food' : food,
        'id' : id
    }
    return render(request, 'food/details.html',context)

@login_required(login_url='signin')
def add_to_cart(request):
    if request.method == "POST":
        id = request.POST.get("food_id")
        quantity = request.POST.get("quantity")
        food_items = {}
        if request.session.get("food_items"):
            food_items = request.session.get("food_items")
        food_items[id] = quantity
        request.session["food_items"] = food_items
        print(request.session["food_items"])
    return redirect('menu')

@login_required(login_url='signin')
def cart(request):
    food_items = request.session.get("food_items")
    items = []
    total_price = 0
    if food_items:
        for id,quantity in food_items.items():
            food = Food.objects.get(id=id)
            price = int(quantity) * int(food.price)
            total_price += price
            items.append({
                "id":id,
                "name":food.name,
                "quantity":quantity,
                "price":price,
                "photo":food.image
            })
    context = {
        "foods":items,
        "total_price":total_price
    }
    return render(request, 'food/cart.html', context)

@login_required(login_url='signin')
def delete_cart_item(request, id):
    food_items = request.session.get("food_items")
    del food_items[id]
    request.session["food_items"] = food_items
    return redirect('cart')

@login_required(login_url='signin')
def check_out(request):
    if not request.session.get("OTP"):
        otp = randint(111111,999999)
        send_mail(
            "OTP from SIT-CAFE",
            f"Your OTP to order food from SIT-CAFE is {otp}",
            "mohansaip2001@gmail.com",
            [request.user.email,],
            fail_silently=False
        )
        request.session["OTP"] = otp
    return render(request,'food/check_out.html')

@login_required(login_url="signin")
def place_order(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        if request.session.get("OTP") != int(otp):
            messages.error(request, "Invalid OTP")
            return redirect('check_out')
        else:
            foods = request.session.get("food_items")
            if foods:
                order_details = ""
                total_price = 0
                for id,quantity in foods.items():
                    food = Food.objects.get(id=id)
                    price = food.price * int(quantity)
                    total_price += price
                    order_details += f"{food.name} x {quantity}"
                order = Order(user=request.user,order_details=order_details,total_price=total_price)
                order.save()
                del request.session["food_items"]
                del request.session["OTP"]
        
    return redirect('orders')

@login_required(login_url='signin')
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    context = {
        "orders": orders
    }
    return render(request, 'food/orders.html', context)