from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    analyzed = djtext  # Start with the original text
    params = {}

    if removepunc == "on":
        analyzed = "".join(char for char in analyzed if char not in punctuation)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    if fullcaps == "on":
        analyzed = analyzed.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = "".join(char for char in analyzed if char not in ["\n", "\r"])
        params = {'purpose': 'New line Remover', 'analyzed_text': analyzed}

    if spaceremove == "on":
        analyzed = " ".join(analyzed.split())
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}

    if charcounter == "on":
        char_count = len(analyzed)
        params = {'purpose': 'Character Count', 'analyzed_text': char_count}

    # If no operation was selected, return a message
    if not params:
        params = {'purpose': 'No operation selected', 'analyzed_text': 'Please select an operation.'}

    return render(request, "analyze.html", params)