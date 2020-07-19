from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homePage(request) :                     # this is like Rest handler function, it corresponding 'url' is defined in
    return HttpResponse("Welcome!!!!!!")    #           'urls.py' in current directory.


def htmlTextContent(request) :
    return HttpResponse("<h> Welcome.......... </h>")


# we have configured ''DIRS': [os.path.join(BASE_DIR, 'myApp/templates')]' in 'settings.py'
def htmlTemplateContent(request) :
    return render(request, 'WelcomeHtml.html', {'username' : 'Yatish'}) # parameter 'username' will be resolved to 'Yatish'
                                                                        # in 'WelcomeHtml.html' file in {{username}}



def addition(request) :
    return render(request, 'Addition.html');



def additionResult(request) :               # here we are getting the query parameters using 'GET[<PARAMETER_NAME>]'
    a = int(request.GET["num1"])
    b = int(request.GET["num2"])
    res = a + b
    return render(request, 'AdditionResult.html', {'result' : res})



def additionResultPOST(request) :               # here we are getting the query parameters using 'POST[<PARAMETER_NAME>]'
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    res = a + b
    return render(request, 'AdditionResult.html', {'result' : res})



def downloadedTravelloTemplate(request) :
    return render(request, 'index.html')