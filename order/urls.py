from django.urls import path
from order.views import CartView

urlpatterns = [
    path('/carts',CartView.as_view())
]
