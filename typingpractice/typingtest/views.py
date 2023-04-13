from django.shortcuts import render
from .forms import TypingForm
from .models import MovieScene

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
        data = request.POST['response']
            
    return render(request, 'typingtest/results.html', {'form': TypingForm(), 'data':data})
