"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from movies.views import movies_about, my_movies
from my_app.views import about, hello, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("about/", about),
    # Dynamic routes
    path("hello/<str:first_name>/", hello),

    # Movies App routes
    path("movies/", my_movies, name='home'),
    path("movies/about", movies_about, name='about'),

    # Job board routes using include
    path("jobs/", include("job_board.urls"))
]
