'''

We need to update this file in the main 'urls.py' file of the project.

'''


from django.urls import path
from . import views     # we are importing 'views.py' from current directory i.e. '.'

# Remember all the urls we specify doesn't start with '/', it comes at end. eg: '/htmlText' gives error correct is
#       'htmlText/'
urlpatterns = [
    path('', views.homePage, name = 'myHomePage'),  # we need to define 'homePage' function in 'views.py'. similarly for
    path('htmlText/', views.htmlTextContent, name = "htmlText"),                                    # below url mappings
    path('htmlTemplate/', views.htmlTemplateContent, name = "WelcomeHtml"),
    path('addition/', views.addition, name = "addition"),
    path('addition/additionResult/', views.additionResult, name = "additionResult"),
    path('addition/additionResultPOST/', views.additionResultPOST, name = "additionResultPOST"),
    path('travello/', views.downloadedTravelloTemplate, name = "downloadedTravelloTemplate")
]
