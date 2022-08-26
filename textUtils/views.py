# i have created this file
from ast import Param
from hashlib import new
from os import remove
from string import punctuation
from tkinter.dnd import DndHandler
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    
    #check box values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    removespace = request.GET.get('removespace','off')
    countchar = request.GET.get('countchar','off')
    
    
    if removepunc == "on":
        print(removepunc)
        punctuation =''':;()*&^%$#@!~`-_=+[]{}'";:,<.>?/\|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed += char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed,'real_text':djtext}
        #analay the text
        return render(request,'analyze.html',params)
    
    elif fullcaps == 'on':
        new_text= djtext.upper()
        params={'purpose':'Converted Text into UpperCase','analyzed_text':new_text,'real_text':djtext}
        #analay the text
        return render(request,'analyze.html',params)
    
    elif newlineremover == 'on':
        new_text = ''
        for x in djtext:
            if x !='\n':
                new_text = new_text + x
        params={'purpose':'Remove New Line','analyzed_text':new_text,'real_text':djtext}
        #analay the text
        return render(request,'analyze.html',params)
    
    elif removespace == 'on':
        new_text = djtext.replace('  ',' ')
        params={'purpose':'Remove Space','analyzed_text':new_text,'real_text':djtext}
        #analay the text
        return render(request,'analyze.html',params)
    
    elif countchar == 'on':
        No = len(djtext) - djtext.count(' ')
        params={'purpose':'Numbers of Characters','analyzed_text':No,'real_text':djtext}
        #analay the text
        return render(request,'analyze.html',params)
    
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capfirst") 

# def newlineremove(request):
#     return HttpResponse("newlineremove") 

# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>") 

# def charcount(request):
#     return HttpResponse("charcount") 
