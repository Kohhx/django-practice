from django.shortcuts import render

# Create your views here.
def my_movies(request):
    context = {
        'movies': [
            'The Matrix',
            'Top Gun'
        ]
    }
    return render(request, "movies/movies.html", context)

def movies_about(request):
    return render(request, "movies/about.html")
