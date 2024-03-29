from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404

from .models import Product,Image,Customer, Cart, OrderItem, Order
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm, OrderCreateForm
# Create your views here.

def first_page(request):
    return render(request,'mainapp/main.html',None)

def order_place_succ(request):
    return render(request,'mainapp/order_place_succ.html',None)

def intro_page(request):
    return render(request,'mainapp/intro.html',None)


def prod_table(request):
    query_results=Product.objects.all()
    return render(request,'mainapp/prodTable.html',None)

def cust_table(request):
    query_results=Customer.objects.all()
    return render(request,'mainapp/custTable.html',None)

def order_table(request):
    query_results=Order.objects.all()
    return render(request,'mainapp/orderTable.html',None)

def main_detail(request):
    return redirect('first_page')
#------------------------------------------------------------------
#---------WOMEN----------------------------------------------------
def full_page(category):
    all_images = Image.objects.all()
    all_items = []
    for img in all_images:
        if (img.product.category == category) and (img.product not in all_items):
            img.product.image = img.image
            all_items.append(img.product)
    return all_items

class ShirtsView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Shirt")

    def get_context_data(self, **kwargs):
        context = super(ShirtsView, self).get_context_data(**kwargs)
        context['title'] = "SHIRTS"
        context['name'] = "shirts"
        return context

class DressesView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Dress")

    def get_context_data(self, **kwargs):
        context = super(DressesView, self).get_context_data(**kwargs)
        context['title'] = "DRESSES"
        context['name'] = "dresses"
        return context


class SweatersView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Sweater")

    def get_context_data(self, **kwargs):
        context = super(SweatersView, self).get_context_data(**kwargs)
        context['title'] = "SWEATERS"
        context['name'] = "sweaters"
        return context


class CoatsView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Coat")

    def get_context_data(self, **kwargs):
        context = super(CoatsView, self).get_context_data(**kwargs)
        context['title'] = "COATS"
        context['name'] = "coats&jackets"
        return context


class SkirtsView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Skirt")

    def get_context_data(self, **kwargs):
        context = super(SkirtsView, self).get_context_data(**kwargs)
        context['title'] = "SKIRTS"
        context['name'] = "skirts"
        return context


class JeansView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Jeans")

    def get_context_data(self, **kwargs):
        context = super(JeansView, self).get_context_data(**kwargs)
        context['title'] = "JEANS"
        context['name'] = "jeans"
        return context

#--------------------------------------------------------------------------

def details(request,category,item_id):
    all_prod = Product.objects.all()
    all_images = Image.objects.all()
    all_items = all_prod.filter(category=category)
    my_images = []
    myItem = all_items.get(productID=item_id)
    for img in all_images:
        if (img.product == myItem):
            my_images.append(str(img.image))
    template = loader.get_template('mainapp/details.html')
    context = {'myItem': myItem, 'my_images': my_images}
    return HttpResponse(template.render(context, request))


def shirt_detail(request,shirt_id):
    return details(request,"Shirt",shirt_id)

def dress_detail(request,dress_id):
    return details(request,"Dress", dress_id)

def sweater_detail(request,sweater_id):
    return details(request,"Sweater", sweater_id)

def coat_detail(request,coat_id):
    return details(request,"Coat", coat_id)

def jean_detail(request,jean_id):
    return details(request,"Jeans", jean_id)

def skirt_detail(request,skirt_id):
    return details(request,"Skirt", skirt_id)

#---------------------------------------------------------------------
#-------------MEN----------------------------------------------------

class TshirtView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Tshirts")

    def get_context_data(self, **kwargs):
        context = super(TshirtView, self).get_context_data(**kwargs)
        context['title'] = "T-SHIRTS"
        context['name'] = "tshirts"    # URL : /tshirts/..
        return context


class HoodieView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Hoodies")

    def get_context_data(self, **kwargs):
        context = super(HoodieView, self).get_context_data(**kwargs)
        context['title'] = "HOODIES"
        context['name'] = "hoodies"
        return context


class MjeansView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("Mjeans")

    def get_context_data(self, **kwargs):
        context = super(MjeansView, self).get_context_data(**kwargs)
        context['title'] = "JEANS"
        context['name'] = "Mjeans"
        return context

class MjacketsView(generic.ListView):
    template_name = 'mainapp/items.html'

    def get_queryset(self):
        return full_page("MCoats")

    def get_context_data(self, **kwargs):
        context = super(MjacketsView, self).get_context_data(**kwargs)
        context['title'] = "COATS & JACKETS"
        context['name'] = "Mjackets"
        return context


#---------------------------------------------------------------------

def tshirt_detail(request,tshirt_id):
    return details(request,"Tshirts",tshirt_id)

def hoodie_detail(request,hoodie_id):
    return details(request,"Hoodies",hoodie_id)

def Mjeans_detail(request,Mjean_id):
    return details(request,"MJeans",Mjean_id)

def Mjackets_detail(request,Mjacket_id):
    return details(request,"MCoats",Mjacket_id)

#------------------------------------------------------------------------------
def cart_page(request):
    return render(request, 'mainapp/cart.html', None)
def order_page(request):
    return render(request, 'mainapp/order.html', None)

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            first_name=form['first_name'].value()
            last_name=form['last_name'].value()
            username=form['username'].value()
            email=form['email'].value()
            password=form['password1'].value()
            customer=Customer(user=user,username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            customer.save()
            return redirect('/log_in/')
           # return redirect('/profile/'+str(customer.pk))
        else:
            args = {'form': form}
            return render(request, 'mainapp/customer_form.html', args)
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'mainapp/customer_form.html',args)

def place_order(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                first_name = form['first_name'].value()
                last_name = form['last_name'].value()
                email = form['email'].value()
                address = form['address'].value()
                city = form['city'].value()
                order = Customer(first_name = first_name,last_name =last_name,email = email,address = address,city = city)
                order.save()
                return redirect('/log_in/')
            else:
                args = {'form': form}
                return render(request, 'mainapp/main.html', args)




def profile(request,id):
    #args={'user':request.user}
    customer = get_object_or_404(User, pk=id)
    return render(request,'mainapp/customer_profile.html',{'user':customer})

#------------------------------------------------------------------------------------------------

def stores(request):
    return render(request, 'mainapp/stores.html', None)

def policies(request):
    return render(request, 'mainapp/policies.html', None)

def contact(request):
    return render(request, 'mainapp/contact.html', None)

#-------order

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            request.session['order_id'] = order.id


    else:
        form = OrderCreateForm()
    return render(request,
                  'mainapp/order.html',
                  {'cart': cart, 'form': form})
# ----------cart

def cart(request):
    return{'cart': Cart(request)}

def product_detail(request, product_id):
    product = get_object_or_404(Product,productID=product_id,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'mainapp/detail.html', {'product': product,'cart_product_form': cart_product_form})



@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=product_id)
    form = CartAddProductForm(request.POST,product)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('mainapp:cart_detail')

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=product_id)
    form = CartAddProductForm(request.POST,product)
    cart.add(product=product,quantity=1,
                 update_quantity='true')
    return redirect('mainapp:cart_detail')




def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=product_id)
    cart.remove(product)
    return redirect('mainapp:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})
    return render(request, 'mainapp/cart.html',{'cart': cart})








