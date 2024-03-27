# myapp/views.py

from django.shortcuts import render
from .models import Item, FAQ
from .forms import SearchForm

def index(request):
    output = ''
    
    if request.method == 'GET':
        form = SearchForm(request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            items = Item.objects.filter(name__icontains=search_query)
            
            if items:
                output = '\n'.join([f"{item.name} - {item.description}" for item in items])
            else:
                output = 'No items found'
    else:
        form = SearchForm()
    
    context = {
        'form': form,
        'output': output,
    }
    return render(request, 'index.html', context)

def question(request):
    output = ''
    
    if request.method == 'GET':
        form = SearchForm(request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            questions = FAQ.objects.filter(question__icontains=search_query)  # Corrected query
            
            if questions:
                output = '\n'.join([f"{item.question} - {item.answer} - {item.reference} - {item.image}" for item in questions])      # Corrected output generation
            else:
                output = 'No items found'
    else:
        form = SearchForm()
    
    context = {
        'form': form,
        'output': output,
    }
    return render(request, 'question.html', context)
