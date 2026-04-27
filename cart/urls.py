from django.urls import path
from .views import add_to_cart, remove_cart_item, update_cart_item, view_cart

urlpatterns = [
    path('add/', add_to_cart),
    path('', view_cart),
    path('update/<int:item_id>/', update_cart_item),
    path('remove/<int:item_id>/', remove_cart_item),
]