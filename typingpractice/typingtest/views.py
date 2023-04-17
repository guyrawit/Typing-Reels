from django.shortcuts import render
from .forms import TypingForm
from .models import MovieScene
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def index(request):
    return render(request, 'typingtest/index.html')

def start(request):
    random_movie = MovieScene.objects.order_by('?').first()
    print(random_movie.title)
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
    return render(request, 'typingtest/results.html', context)
