from django.http import HttpResponse
from django.shortcuts import render

def introduce(request):
    text = request.GET.get('text', '')
    return render(request, 'postal_card.html', {'postal_card_text': text})
