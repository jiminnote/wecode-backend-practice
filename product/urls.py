from django.urls import path
from product.views import ProductdetailView

urlpatterns = [
    path('/<int:product_id>',ProductdetailView.as_view()),
]
