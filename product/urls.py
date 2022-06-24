from django.urls import path
from product.views import ProductdetailView

urlpatterns = [
    #path('/productdetail',ProductdetailView.as_view()),
    path('/<int:product_id>',ProductdetailView.as_view()),
]
