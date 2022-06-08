import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results=[]
        for actor in actors:
            results.append(
            {
                "name" : actor.first_name + ' ' + actor.last_name,
                "movie list" : [{"movie" : movie.title} for movie in actor.movie.all()]
            }
        )
        return JsonResponse({'result':results}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results=[]
        for movie in movies:
            results.append(
            {
                "title" : movie.title,
                "running time" : movie.running_time
            }
        )
        return JsonResponse({'result':results}, status=200)