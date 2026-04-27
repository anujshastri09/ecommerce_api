from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction

from cart.models import CartItem
from .models import Order, OrderItem
from .serializers import OrderSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic   # 🔥 VERY IMPORTANT
def place_order(request):
    user = request.user
    cart_items = CartItem.objects.filter(cart__user=user)

    if not cart_items.exists():
        return Response({"error": "Cart is empty"}, status=400)

    total_price = 0
    order = Order.objects.create(user=user)

    for item in cart_items:
        product = item.product

        # ❌ Check stock
        if product.stock < item.quantity:
            return Response(
                {"error": f"Not enough stock for {product.name}"},
                status=400
            )

        # ✅ Reduce stock
        product.stock -= item.quantity
        product.save()

        # ✅ Create order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity
        )

        total_price += product.price * item.quantity

    # ✅ Save total price
    order.total_price = total_price
    order.save()

    # ✅ Clear cart
    cart_items.delete()

    return Response({
        "message": "Order placed successfully",
        "order_id": order.id
    })

# Create your views here.
