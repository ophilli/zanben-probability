from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import InputForm
from .compute import compute

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(request, form)
    else:
        form = InputForm()
    return render(request,'cards/cards.html', {'form':form})

def present_output(request, form):
    deckSize = form.deckSize
    numCardsInCategory = form.numCardsInCategory
    numAtLeast = form.numAtLeast
    numDraws = form.numDraws

    prob = compute(deckSize, numCardsInCategory, numAtLeast, numDraws)
    form.Prob = prob
    return render(request, 'cards/cards.html', {'form':form})
