'''

DB integration
--------------
    We can integrate Django to DB like how we do in java. Django acts as Hibernate as well. it creates tables
    based on our model classes (ORM)


Steps to configure DB connection
--------------------------------
    By default when project skeleton is created. In 'settings.py' we get dummy 'mySql' configs. We need to override with
    following configs to point to postgres SQL.

            DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': 'yatishDB',
                        'USER': 'postgres',
                        'PASSWORD': '1234'
                        'HOST': 'localhost'
                 }
            }

    NOTE: Like how we have JDBC connector. we need to install a postgress connector called 'psycopg2' package using 'pip'


Like Hibernate in python it doesn't create the tables based on the 'pojo's we have. We need to manually do that using
few commands as shown in below steps.


Steps to Create Tables based on the model/pojo classes we have
--------------------------------------------------------------
    We need to write class in 'models.py' under 'myApp'. You can refer to the 'models.py' file for the class 'Destination'
    for which the table 'Destination' has to be created.

    NOTE : we need to extend the model/table classes with 'models.Model'
    NOTE : we cannot use normal data types like 'name : str'. we have to assign them the 'models.' types which is
            understood by Django. we need to use '=' not ':' while assigning types for data members.

    Once we have the models ready, then we need to execute following command to create content under 'migrations' folder,
            ' python manage.py makemigrations'
        This command will create '0001_initial.py' file under 'migrations' folder.

        NOTE: This command might give error as we are uploading image, so we need to install 'Pillow' package using pip.

    Then we will execute following command to actually create sql statements from '0001_initial.py' file,
            'python manage.py sqlmigrate myApp 0001'  --> This is optional
    Then to execute that sql statements to DB, we need to execute following command,
            'python manage.py migrate'
    This command doesn't only push sql statements in 0001 but if that execute sql statements in all the files in
        'migrations' folder to DB.


NOTE: once you migrate, and later you want to do any further change to models or add or remove a class/table. Then
        you need to re-migrate with the same steps. but you will get different file created under 'migrations'
        folder which could be '0002_xxxxxxx.py'.



For get all objects from DB?
        '<MODEL_CLASS>.objects.all()' this code will get all the rows as of list of objects.
            eg: 'Destination.objects.all()'

For saving object to DB?
        '<OBJECT>.save()' this code will save the current object.
            eg: 'destination1.save()'


For getting an object based on condition?
        '<MODEL_CLASS>.objects.filter(<CONDITION)'
            eg: 'Destination.objects.filter(name = "Bangalore")'
        NOTE: we can use 'exists()' also to check if any row/result exist. This will return boolean result.
                    eg: 'Destination.objects.filter(name = "Bangalore").exists'




NOTE: Django admin UI also supports the saving/update of rows to DB using following steps
    We can use the 'admin UI' as explained in '5_AdminPanel.py'. It will show the Objects/Tables on clicking corresponding
    table, we can input the row values and save but for table to appear here we have to
        register the model in 'admin.py' in 'myApp'. in this code we see that we have registered 'Destination' model
        using code 'admin.site.register(Destination)'.

        
NOTE: If we are using media(image/videos) to be saved in DB then we need to configure where it need to be saved to. Then
        we need to configure in 'settings.py' which are 'MEDIA_URL' and 'MEDIA_PATH'. and then map this URL in 'urls.py'
        of main project.






'''