from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item,Order,OrderItem
from django.utils import timezone

class HomeView(ListView):
    model = Item
    paginate_by=10
    template_name="home.html"

class ProductDetailView(DetailView):
    model= Item
    template_name="product.html"

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
            messages.info(request, "This item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")

    else:
        ordered_date=timezone.now()
        order= Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("core:product",slug=slug)

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
    messages.info(request, "This item was removed from your cart.")
    return redirect("core:product",slug=slug)
    
class CheckOutView(ListView):
    model=Item
    template_name="checkout.html"
