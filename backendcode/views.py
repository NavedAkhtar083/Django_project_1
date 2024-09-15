# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request, 'index.html')

# return HttpResponse("Home")

# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
# def analyze(request):

#    #Get the text

#    djtext = request.GET.get('text', 'default')

# def analyze(request):
    
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     analyzed=djtext
#     params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
#     return render(request,'analyze.html',params)

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    uppercase=request.GET.get('uppercase','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
            
        params = {'purpose': 'upper case letter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')