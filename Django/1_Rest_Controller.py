'''

Rest Controller
---------------
Rest controller are the request handlers.

How to write the Rest Controllers in python?
    In this project we have written following REST controllers in 'views.py',
        1) 'homePage()'
            -----------
            This handler is mapped to url '' in 'urls.py'.
            This is returning a string in 'HttpResponse' object.

        2) 'htmlTextContent()'
            ------------------
            This handler is mapped to url 'htmlText/' in 'urls.py'
            This is returning a string which is of HTML format in 'HttpResponse' object.

        3)  'htmlTemplateContent()'
            -----------------------
            This handler is mapped to url 'htmlTemplate/' in 'urls.py'
            This is returning .html file using 'render()' method.
            NOTE: we need to first configure the path of html templates/files in 'settings.py' under 'Templates' in
                    'DIRS' property value.

    ***** Refer to 'views.py' and 'urls.py' to learn all the REST handlers. *****


    NOTE: We have mapped the 'urls.py' under 'MyApp' folder in the 'urls.py' of the root project directory.
    NOTE: We use 'GET["<PARAMETER_NAME>"]' on request object to get the query parameter in GET calls
    NOTE: We use 'POST["<PARAMETER_NAME>"]' on request object to get the parameter values in POST calls


'''