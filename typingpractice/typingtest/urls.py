from django.urls import path
from . import views

app_name = 'typingtest'

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('congratulation/', views.congratulation, name='congratulation'),
    path('save_score/', views.save_score, name='save_score'),
    # path('typing/', views.typing, name='typing'),
    path('results/', views.results, name='results'),
    path('movies/', views.movies, name='movies'),
    path('start/<int:movie_id>/', views.start_movie, name='start_movie'),
    ]
