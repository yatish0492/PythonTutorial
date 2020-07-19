'''

Here we will import an UI template and integrate to our project
---------------------------------------------------------------
    We are integrating the template present at - https://colorlib.com/wp/template/travello

    We have copied the files under folder 'Travello_Downloaded_Template'. one handler 'downloadedTravelloTemplate()'
        in 'views.py' is returning the 'index.html' inside 'Travello_Downloaded_Template' folder. we have added this
        folder into the 'DIRS' property of 'TEMPLATES' in 'settings.py'. In 'urls.py' we have mapped URL 'travello/'
        to this handler.

    When we called url 'travello/' url. it didn't load UI, it gave errors like it is not able to find 'jquery' and other
    scripts. What to do?
        The reason why was because it sends only 'index.html' and doesn't send any supporting scripts and images to UI.
        To do that. we need to do following to declare them as static so that python loads all these files to UI.
            1) Declare the path of these files as 'static' in 'settings.py' as shown below,
                    'STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myApp/Travello_Download_Template')]
                    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
                Django will copy all the files which we need into 'assets' folder so it picks all the files which are
                required in the html file from here.
                we need to execute following command to copy the files to 'assets',
                    'python manage.py collectstatic'

                                                OR

                we could have manually copied the files into 'assets' file and then specify
                    'STATIC_ROOT = os.path.join(BASE_DIR, 'assets')' in 'settings.py'



            2) In 'index.html' where ever we are refering to the files in 'assets' we need to put code as follows,
                    {% static '<FILE_PATH>' %}
               and we need to give following code at top of the 'index.html' file.
                    {% load static %}


'''