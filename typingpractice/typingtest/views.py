from django.shortcuts import render
from .forms import TypingForm


def index(request):
    return render(request, 'typingtest/index.html')

def start(request):
    form = TypingForm()
    context = {'form': form}
    return render(request, 'typingtest/start.html', context)

# def typing_view(request):
    
def results(request):
    data = None
    if request.method == "POST":
        data = request.POST['response']
            
    return render(request, 'typingtest/results.html', {'form': TypingForm(), 'data':data})
