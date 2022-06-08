import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor

class ActorView(View):
    def get(self, request):
        results=[]
        for actor in Actor.objects.all():
            results.append(
            {
                "name" : actor.first_name + actor.last_name,
                "movie list" : [ movie.title for movie in actor.movies.all()]
            }
        )
        return JsonResponse({'result':results}, status=200)

class MovieView(View):
    def get(self, request):
        results=[]
        for movie in Movie.objects.all():
            results.append(
            {
                "title" : movie.title,
                "running time" : movie.running_time,
                "actors" :  [movie.first_name + movie.last_name for movie in movie.actor_set.all()]
               
            }
        )
        return JsonResponse({'result':results}, status=200)
    