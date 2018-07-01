from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "uStudy - the best study site in the world"
    today = 'tuesday'

    context = {'our_greeting':greeting, 'day_of_week':today} #just an empty dictionary

    return render(request, 'home.html', context)