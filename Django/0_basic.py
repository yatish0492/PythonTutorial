'''

Django
------
    Django is a web framework of python. It follows MVT(Model View Template), Not MVC.
        Model - this is the one which is mapped with the data ORM from DB. Same as model in MVC
        view - View acts as as controller in MVC. it does the business logic
        Template - this acts as View in MVC. it give html/template files used to show on UI.



    Django comes with a light weight server, we can bring up using this server using 'python manage.py runserver'

Steps to create Django Project
------------------------------
    1) To create the base skeleton project we need to execute 'django-admin startproject django_tutorial_project'
         this will create following files in the skeleton project explained as follows,
            'manage.py' --> This is the file which has the script for bringing up or managing the server or you can
                            say manging the project.
            'settings.py' --> This has the settings about the project like 'Debug = True' etc. It has database settings
                              like url, username and password etc.
            'urls.py' --> This has the url mappings like the servlet mappings we have in java. it has contents like,
                          eg: '/home' mapped to 'views.home' here 'views' is a python file 'views.py' and 'home' is
                                a function which takes input request object and returns the response Object.


Steps to create Modules/Apps in Django Project
----------------------------------------------
    1) To create the module/apps in the Django project, we need to execute 'python manage.py startapp <App_Name>'
            eg: 'python manage.py startapp myApp'
        this will create following files in the skeleton project under folder <App_Name> explained as follows,
            'models.py' --> This model files are same as that of java, used for ORM.
            'views.py' --> This file will have functions similar to REST controllers, which will accept the
                            request object and return back the response objects.

    * we can create 'urls.py' at each app level if we want to specify the url mappings for that app in here and then
        we need to update this 'urls.py' path in main project's 'urls.py' file
                                    OR
        we can specify all the url mappings inside the main 'urls.py' file. which is not recommended as that will become
        messy and not clean.
    * The app will not have 'settings.py' because settings are available at root project level not at every
        module/app level.

    NOTE: once we create the app, we need to add that app name to the list 'INSTALLED_APPS' in 'settings.py'. You can
            see that we have added 'myApp' in the list in 'settings.py'

How does this server know how to handle the urls, what to respond?
    It will goto 'urls.py' file and there we have all url mappings accordingly it will call corresponding handler
    functions. if we are mapping an URL to another 'urls.py' file then it goes to that file and in that it will
    find the corresponding handler function.



NOTE: We have other python frameworks instead of Django like 'Flask' etc.

    Why do we use Django when we have other frameworks?
        Due to following advantages,
            1) Fast - It provides auto configurations like spring boot so that we can develop faster.
            2) Components - Many components available to help with any feature we want
            3) Security
            4) Scalability

        To create Django skeleton project to get started on a new app.
'''

