<<<<<<< HEAD
from django.urls import path
from product.views import ProductListView

urlpatterns = [
   path('', ProductListView.as_view())
]
=======


from django.urls import path
from product.views import CategoryView

urlpatterns = [
    path('/categories',CategoryView.as_view()),
]

>>>>>>> main
