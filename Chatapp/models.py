from django.db import models

# Create your models here.


from django.db import models

class User(models.Model):
    # Other fields...
    Username = models.CharField(max_length=100)
    
    # Other fields...

