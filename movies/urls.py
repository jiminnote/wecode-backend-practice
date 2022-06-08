from django.urls   import path
from movies.views     import MovieView, ActorView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view()),
    
]