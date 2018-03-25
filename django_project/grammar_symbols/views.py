from django.shortcuts import render
from django.http import HttpResponse

import spacy
nlp = spacy.load('en')

def index(request):
	doc = nlp("Jackson is, of course, better than Grant.")
	words = [{'token': token, 'file': 'grammar_symbols/{0}.svg'.format(token.pos_)} for token in doc]
	return render(request, 'grammar_symbols/index.html', {'words': words})