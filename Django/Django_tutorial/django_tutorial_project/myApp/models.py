from django.db import models

# Create your models here.

# we need to extend the model/table classes with 'models.Model'
# we cannot use normal data types like 'name : str'. we have to assign them the 'models.' types which is understood by
#       Django.
#
# NOTE : we need to use '=' not ':' while assigning types for data members.
class Destination(models.Model) :

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')   # uploads  to 'pics' folder.
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

