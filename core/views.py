from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from .models import Item,Order,OrderItem,Address
from .forms import CheckoutForm
from django.utils import timezone

class HomeView(ListView):
    model = Item
    paginate_by=10
    template_name="home.html"

class OrderSummaryView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        #To check if order is there or not
        try:
            order=Order.objects.get(user=self.request.user,ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html',context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

        
class ProductDetailView(DetailView):
    model= Item
    template_name="product.html"

@login_required
def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item, created=OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    #to check if user has ordered or not
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        #to check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)

    else:
        ordered_date=timezone.now()
        order= Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product",slug=slug)

@login_required
#For the addition of the item in the ordersummary page 
def add_single_item_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item, created=OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    #to check if user has ordered or not
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        #to check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)

    else:
        ordered_date=timezone.now()
        order= Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:order-summary")

@login_required
def remove_from_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    #to check if user has ordered or not
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        #to check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:

                order_item.quantity -= 1

                order_item.save()
            else:
                order_item.delete()
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product",slug=slug)

    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product",slug=slug)
    return redirect("core:product",slug=slug)

#For the deletion of the item in the ordersummary page 
@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

class CheckOutView(View):
    def get(self,*args,**kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request,"checkout.html",context)
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order=Order.objects.get(user=self.request.user,ordered=False)
            if form.is_valid():
                street_address=form.cleaned_data.get("street_address")
                apartment_address = form.cleaned_data.get("apartment_address")
                zip_code = form.cleaned_data.get("zip_code")
                state = form.cleaned_data.get("state")
                country= form.cleaned_data.get("country")
                # TODO add functionalities later
                #same_billing_address =form.cleaned_data.get("same_billing_address")
                #save_info = form.cleaned_data.get("save_info")
                payment_option =form.cleaned_data.get("payment_option")
                address=Address(user=self.request.user,
                                street_address=street_address,
                                apartment_address=apartment_address,
                                country=country,
                                zip_code=zip_code,
                                state=state
                )
                address.save()
                order.address=address
                order.save()
                print(form.cleaned_data)
                return redirect('core:checkout')
            messages.warning(self.request,"Failed Checkout")
            return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")