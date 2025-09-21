from django.urls import path
from users.views import SignupView,SigninView, UserView
urlpatterns = [
    path('/signup',SignupView.as_view()),
    path('/signin',SigninView.as_view()),
    path('/mypage',UserView.as_view())
]