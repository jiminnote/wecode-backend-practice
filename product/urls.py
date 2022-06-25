from django.urls import path
from product.views import CategoryView

urlpatterns = [
    #path('/productdetail',ProductdetailView.as_view()),
    path('/category',CategoryView.as_view()),
]

