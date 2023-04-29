from django.shortcuts import render
from .forms import TypingForm
from .models import MovieScene, UserScore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from django.http import HttpResponseBadRequest
import hashlib
import random
from django.shortcuts import redirect, reverse
import json

def index(request):
    movie_list = list(MovieScene.objects.values_list('id', flat=True))
    request.session['movie_list'] = movie_list
    return render(request, 'typingtest/index.html')

def start(request):
    if 'movie_list' not in request.session:
        movie_list = list(MovieScene.objects.values_list('id', flat=True))
        request.session['movie_list'] = movie_list
    else:
        movie_list = request.session['movie_list']
    
    if not movie_list:
        # All movies have been played, redirect to a new page
        return redirect(reverse('typingtest:congratulation'))
    random_movie_id = random.choice(movie_list)
    movie = MovieScene.objects.get(pk=random_movie_id)
    form = TypingForm()
    context = {'form': form, 'movie': movie}
    return render(request, 'typingtest/start.html', context)

def start_movie(request, movie_id):
    random_movie = MovieScene.objects.get(id=movie_id)
    form = TypingForm()
    context = {'form': form, "movie": random_movie}
    return render(request, 'typingtest/start.html', context)

# def typing_view(request):
    
def results(request):
    data = None
    if request.method == "POST":
        data_original = request.POST['response']
        movie_id = request.POST['movie_id']
        movie = MovieScene.objects.get(id=movie_id)
        data = re.sub(r'[^\w\s]', '', data_original.lower())
        transcript = re.sub(r'[^\w\s]', '', movie.transcript.lower())
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([data , transcript])
        accuracy = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]*100
        accuracy = str(accuracy)[:4]
        context = {'data': data_original, 'movie': movie, 'accuracy':accuracy}
        if 'movies' not in request.session:
            request.session['movies'] = {}
        request.session['movies'][movie_id] = float(accuracy)
        
        context = {'data': data_original, 'movie': movie, 'accuracy': accuracy}
        
        movie_list = request.session['movie_list']
        if movie.id in movie_list:
            movie_list.remove(movie.id)
            request.session['movie_list'] = movie_list
        print(request.session['movies'])  
        print(request.session['movie_list'])
        return render(request, 'typingtest/results.html', context)
    else:
        return HttpResponseBadRequest()

    


def movies(request):
    objects = MovieScene.objects.order_by('id')[:10]
    context = {"movies":objects}
    return render(request, 'typingtest/movies.html', context)

def leaderboard(request):
    user_scores = UserScore.objects.order_by('-score')[:50]
    context = {'user_scores': user_scores}
    return render(request, 'typingtest/leaderboard.html', context)

def congratulation(request):
    return render(request, 'typingtest/congratulation.html')

def save_score(request):
    if request.method == 'POST':
        if 'movies' not in request.session:
            return redirect('typingtest:index')
        name = request.POST['name']
        accuracy = request.session['movies']
        print(accuracy)
        total_accuracy = 0
        for key, value in accuracy.items():
            total_accuracy += value
            
        avg_accuracy = total_accuracy / len(request.session['movies'])
        
        score = UserScore(name=name, score=avg_accuracy)
        score.save()

        # Delete the session data
        del request.session['movies']

        # Render the leaderboard with the updated data
        user_scores = UserScore.objects.order_by('-score')[:50]
        context = {'user_scores': user_scores}
        return render(request, 'typingtest/leaderboard.html', context)

    # Redirect to index page if the request method is not POST
    return redirect('typingtest:index')
