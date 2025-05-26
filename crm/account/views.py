from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .decoraters import *
from .forms import OrderForm, CreateUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory #more forms inside one form
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@unauthenticate_user
def registerPage(request):
    form = CreateUserForm() #inbuild signup form

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Pass registered user into customer Group
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'account/register.html', context)

def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            group = None
            if user.groups.exists():
                group = user.groups.all()[0].name

            if group == 'admin':
                return redirect('home')  # to dashboard
            elif group == 'customer':
                return redirect('user-page')  # to /user/
            else:
                return HttpResponse("Group not recognized.")
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)

def logoutUser(request):
    # inbuiuld logout function
    logout(request)
    return redirect('login')

def userPage(request):
    context = {}
    return render(request, 'account/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count() 
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 
            'customers': customers,
            'total_customers': total_customers,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending
            }
    
    return render(request, 'account/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()

    return render(request, 'account/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all() # reverse relationship

    myFilter = OrderFilter(request.GET, queryset=orders) #filter the orders match with request
    orders = myFilter.qs #render the orders based on queryset

    context = {'customer': customer, 'orders': orders, 'total_orders': orders.count(), 'myFilter': myFilter}
    return render(request, 'account/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    #multiple forms inside single form
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status')) # extra = 10 Gives 10 more forms
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer}) # prepopulate the form with the customer
    #initial is used to set a form value that shown when for loads
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        # print('Printing POST: ', request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'account/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = get_object_or_404(Order, id=pk) #order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = get_object_or_404(Order, id=pk)  #order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'account/delete.html', context)

def rootRedirectView(request):
    if request.user.is_authenticated:
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return redirect('home')  # dashboard
        elif group == 'customer':
            return redirect('user-page')
        else:
            return HttpResponse("No group assigned.")
    else:
        return redirect('login')



    