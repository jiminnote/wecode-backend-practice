from django.urls import path
from product.views import ProductListView, CategoryView, ProductdetailView

urlpatterns = [
    path('/categories',CategoryView.as_view()),
    path('', ProductListView.as_view()),
    path('/<int:product_id>',ProductdetailView.as_view())
]


