from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .utils import authenticate
from .form import CustomUserCreationForm, UpdateUserForm
from core.models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .form import CheckoutForm



def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user != None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password is incorrect")

    context = {'page': page}
    return render(request, 'core/login_register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('index')

def registerpage(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/login_register.html', {'form': form})

def updateuser(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'core/profile.html', {'form': form})

def userprofile(request):
    page = 'profile'
    form = UpdateUserForm(instance=request.user)
    return render(request, 'core/profile.html', {'page': page, 'form': form})


def index(request):
    return render(request,'core/index.html')
    
def culture(request):
    return render(request,'core/culture.html')

def states_selection(request):
    return render(request,'core/states_selection.html')

def ecommerce(request):
    products=Product.objects.all()
    return render(request,'core/ecommerce.html',{'products':products})

def FCAI(request):
    return render(request,'core/FCAI.html')

def food(request):
    return render(request,'core/food.html')

def harvest_festivals(request):
    return render(request,'core/harvest_festivals.html')

def karnataka(request):
    return render(request,'core/karnataka.html')

def MAH_festivals(request):
    return render(request,'core/MAH_festivals.html')

def maha_clothing_dance_lang(request):
    return render(request,'core/maha_clothing_dance_lang.html')

def mahaculture(request):
    return render(request,'core/mahaculture.html')

def maha_trad(request):
    return render(request,'core/maha_trad.html')

def maharashtra(request):
    return render(request,'core/maharashtra.html')

def religions(request):
    return render(request,'core/religions.html')

def UttarPradesh(request):
    return render(request,'core/UttarPradesh.html')

def agakhan_hotel(request):
    return render(request,'core/agakhan_hotel.html')

def Raigadh(request):
    return render(request,'core/Raigadh_hotel.html')

def shaniwarwada_hotel(request):
    return render(request,'core/shaniwarwada_hotel.html')

def TajMahal_hotel(request):
    return render(request,'core/TajMahal_hotel.html')


def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)

    order_item, created= OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )

    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"Added Quantity Item")

        
        else:
            order.items.add(order_item)
            messages.info(request,"Added Item to Cart")

    
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Added Item to cart")

    return redirect('ecommerce')


# cart page

def order_list_cart(request):
    if Order.objects.filter(user=request.user,ordered=False).exists():
        order=Order.objects.get(user=request.user,ordered=False)
        return render(request,'core/order_list_cart.html',{'order':order})
    
    return render(request,'core/order_list_cart.html',{'message':'Your Cart is Empty!!....'})



def add_item(request,pk):

    product=Product.objects.get(pk=pk)

    order_item, created= OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )

    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            if order_item.quantity < product.product_available_count:
                order_item.quantity +=1
                order_item.save()
                messages.info(request,"Added Quantity Item")
                return redirect("order_list_cart")
            
            else:
                 messages.info(request,"Sorry! Product is out of stock...")
                 return redirect("order_list_cart")
        
        else:
            order.items.add(order_item)
            messages.info(request,"Added Item to Cart")

    
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Added Item to cart")

    return redirect('ecommerce')



def remove_item(request,pk):
   item = get_object_or_404(Product,pk=pk) 
   order_qs=Order.objects.filter(
       user=request.user,
       ordered=False,
   )

   if order_qs.exists():
       order=order_qs[0]
       if order.items.filter(product__pk=pk).exists():
           order_item=OrderItem.objects.filter(
               product=item,
               user=request.user,
               ordered=False,
           )[0]
           
           if order_item.quantity > 1:
               order_item.quantity -= 1
               order_item.save()
           else:
               order_item.delete()
           messages.info(request,"Item quantity was updated")
           return redirect("order_list_cart")
       else:
             messages.info(request,"This item is not in ypur cart")
             return redirect("order_list_cart")
   else:
         messages.info(request,"You do not have any order")
         return redirect("order_list_cart")
   


def checkout(request):
     if CheckoutAdderss.objects.filter(user=request.user).exists():
         return render(request,'core/checkout.html',{'payment_allow':"allow"})
     if request.method == 'POST':
         form = CheckoutForm(request.POST)
         try:
             if form.is_valid():
                 street_address= form.cleaned_data.get('street_address')
                 apartment_address= form.cleaned_data.get('apartment_address')
                 country= form.cleaned_data.get('country')
                 zip_code= form.cleaned_data.get('zip')

                 checkout_address=CheckoutAdderss(
                     user=request.user,
                     street_address=street_address,
                     apartment_address=apartment_address,
                     country=country,
                     zip_code=zip_code,
                     )
                 checkout_address.save()
                 print("It should render the summary page")
                 return render(request,'core/checkout.html',{'payment_allow':"allow"})
         except Exception as e:
             messages.warning(request,"Failed Checkout")
             return redirect('checkout')
         
     else:
         form=CheckoutForm()
         return render(request,'core/checkout.html',{'form':form})

             
         



