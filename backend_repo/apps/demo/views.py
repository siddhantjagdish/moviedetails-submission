from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import Post

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def get_movie_details(request):
    # Fetch movie data from OMDB API
    api_url = "http://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        movie_data = response.json()
        return Response({
            'title': movie_data.get('Title', 'N/A'),
            'year': movie_data.get('Year', 'N/A'),
            'rated': movie_data.get('Rated', 'N/A'),
            'released': movie_data.get('Released', 'N/A'),
            'runtime': movie_data.get('Runtime', 'N/A'),
            'genre': movie_data.get('Genre', 'N/A'),
            'director': movie_data.get('Director', 'N/A'),
            'writer': movie_data.get('Writer', 'N/A'),
            'actors': movie_data.get('Actors', 'N/A'),
            'plot': movie_data.get('Plot', 'N/A'),
            'language': movie_data.get('Language', 'N/A'),
            'country': movie_data.get('Country', 'N/A'),
            'awards': movie_data.get('Awards', 'N/A'),
            'poster': movie_data.get('Poster', 'N/A'),
        })
    except requests.RequestException as e:
        return Response({'error': f'Failed to fetch movie details: {str(e)}'}, status=500)

from django.http import HttpResponse


def home(request):
    return HttpResponse('Welcome to the Movie API!')