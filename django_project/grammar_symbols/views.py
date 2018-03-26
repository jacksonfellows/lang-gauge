from django.shortcuts import render

import spacy
nlp = spacy.load('en')

def index(request):
    if request.method == 'POST':
        words = []
        i = 0
        n = request.POST.get(str(i))
        while n:
            words.append(n)
            i += 1
            n = request.POST.get(str(i))
        doc = nlp(' '.join(words))
    else:
        doc = nlp('')
        
    words = [{'token': token, 'file': 'grammar_symbols/{0}.svg'.format(token.pos_)} for token in doc]
    for i in range(len(words)):
        words[i]['num'] = i
    return render(request, 'grammar_symbols/index.html', {'words': words})