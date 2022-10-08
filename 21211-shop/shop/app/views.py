from django.http import HttpResponse, JsonResponse, Http404
from .models import Order, OrderItem
# from decimal import Decimal

def checkout(request, order_pk):
    try:
        order = Order.objects.get(id=order_pk)
        items = OrderItem.objects.filter(order__id=order_pk)
    except Order.DoesNotExist:
        raise Http404()

    if order:
        total_price = 0

        for item in items:
            total_price += item.product.price * item.quantity
                
        return JsonResponse({"total_price": total_price})
