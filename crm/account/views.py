from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.shortcuts import render, redirect, get_object_or_404

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

def product(request):
    products = Product.objects.all()

    return render(request, 'account/products.html', {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all() # reverse relationship

    context = {'customer': customer, 'orders': orders, 'total_orders': orders.count()}
    return render(request, 'account/customer.html', context)

def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer': customer}) # prepopulate the form with the customer
    #initial is used to set a form value that shown when for loads
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # print('Printing POST: ', request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'account/order_form.html', context)

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

def deleteOrder(request, pk):
    order = get_object_or_404(Order, id=pk)  #order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'account/delete.html', context)


    