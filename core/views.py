from django.shortcuts import render

from core.movies.viewsets import MovieViewSet
from core.actors.viewsets import ActorViewSet
from core.directors.viewsets import DirectorViewSet


def home(request):
    movie_viewset = MovieViewSet()
    actor_viewset = ActorViewSet()
    director_viewset = DirectorViewSet()

    context = {
        'upcoming_movies': movie_viewset.get_upcoming_movies(),
        'popular_movies': movie_viewset.get_popular_movies(),
        'actors': actor_viewset.get_top_actors(),
        'directors': director_viewset.get_top_directors(),
    }

    return render(request, 'core/home.html', context)
