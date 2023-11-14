from django.db import models

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=50)
    phone=models.TextField(max_length=30)
    mail=models.EmailField( max_length=50)
    msg=models.TextField(max_length=10000)
    def __str__(self):
        return self.name