from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from catalog.models import Product
from .models import OrderItem, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


def oder_summary(request):
    profile = request.user.profile
    order = get_object_or_404(Order, profile=profile, ordered=False)
    context = {
        'order': order
    }
    return render(request, 'cart/order.html', context)


@login_required
def create_order(request, pk):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order.ordered = True
            form.save()
            return redirect('cart:complete')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'cart/checkout.html', context)


@login_required
def complete(request):
    return render(request, 'cart/checkout_complete.html')


@login_required
def add_to_cart(request, pk):
    """
    Берем продукт, создаем\\получаем на него продукт заказа(order-item)
    Берем список из ordered-false заказов данного профиля
    Если заказы есть, фильтруем в нём незаказанные продукты.
        Если продукты есть, инкрементируем количество.
        Если продуктов нет, добавляем продукт в корзину.
    Если его нет, создаем заказ, кладем в него продукт заказа.
    """
    product = get_object_or_404(Product, pk=pk)
    profile = request.user.profile
    orderitem, created = OrderItem.objects.get_or_create(
        profile=profile,
        product=product,
        ordered=False,
    )
    orders = profile.get_pending_orders()
    if orders.exists():
        order = orders[0]
        if order.items.filter(product__pk=pk).exists():
            orderitem.quantity += 1
            orderitem.save()
            return redirect('cart:order')
        else:
            order.items.add(orderitem)
            return redirect('cart:order')
    else:
        order = Order.objects.create(profile=profile)
        order.items.add(orderitem)
        return redirect('cart:order')


def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    profile = request.user.profile
    orderitem = OrderItem.objects.get(product=product)
    orders = Order.objects.filter(profile=profile, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.items.filter(product__pk=product.pk).exists():
            if orderitem.quantity > 1:
                orderitem.quantity -= 1
                orderitem.save()
            else:
                order.items.remove(orderitem)
            return redirect('cart:order')
        else:
            return redirect('catalog:categories')
    else:
        return redirect('catalog:categories')











