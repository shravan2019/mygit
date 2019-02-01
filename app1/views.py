from django.http import HttpResponse
from django.shortcuts import render
import operator
# Create your views here.
def homepage(request):
    return render(request, 'app2/home.html',{'name':'sk shravan'})

def count(request):
    data= request.GET['fulltextarea']
    word_list= data.split()
    list_length= len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

            sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1), reverse=True)

    return render(request,'app2/count.html',{'fulltext':data, 'words':list_length, 'worddictionary':sorted_list})

def about(request):
    return render(request,'app2/about.html')
