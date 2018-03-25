from django.shortcuts import render
from django.http import HttpResponse

import spacy
nlp = spacy.load('en')

def index(request):
	doc = nlp("It is reaching out for a better state of society than now exists...a craving for intellectual and moral growth; it is a longing to interpret the laws of creation; it means a wish for less misery among the poor, less ignorance in schools, less bigotry in temple, less suffering in the hospital, less fraud in business, less folly in politics...more study of nature, more love of art, more lessons from history, more security in property, more health in cities, more virtue in country, more wisdom in legislation, more intelligence, more happiness.")
	words = [{'token': token, 'file': 'grammar_symbols/{0}.svg'.format(token.pos_)} for token in doc]
	return render(request, 'grammar_symbols/index.html', {'words': words})