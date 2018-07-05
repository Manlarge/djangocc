from django.shortcuts import (
        HttpResponseRedirect,
        render
)
from .forms import DeckForm
from .models import Deck

#create your views here.
def home(request):
    '''

    Renders the FLASHCARD app home template
    '''

    qs = Deck.objects.order_by('-title').filter(is_active=True)
    context = {'decks': qs}
    return render(request, 'flashcards/home.html', context)

def createDeck(request):

    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm()
    context = {'form': form}
    return render(request,  'flashcards/createDeck.html', context)


def editDeck(request, deck_id):
    '''
    Renders the form to edit information about a deck object
    '''

    deck_object = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form}
    return render(request,  'flashcards/createDeck.html', context)
