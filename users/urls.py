from django.urls import path
from users.views import SignupView,SigninView, MypageView
urlpatterns = [
    path('/signup',SignupView.as_view()),
    path('/signin',SigninView.as_view()),
    path('/mypage',MypageView.as_view())
]