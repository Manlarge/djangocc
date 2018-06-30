from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    context = {} #just an empty dictionary
    return render(request, 'home.html', context=None)