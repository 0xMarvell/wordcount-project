from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordcount_dictionary = {}

    for word in wordlist:
        if word in wordcount_dictionary:
            #increase
            wordcount_dictionary[word] += 1
        else:
            #add to dictionary
            wordcount_dictionary[word] = 1

    sorted_words = sorted(wordcount_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordlist), 'sorted_words': sorted_words})




    
