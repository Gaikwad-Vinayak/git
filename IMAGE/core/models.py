from django.db import models

# Create your models here.
class img(models.Model):
    photo=models.ImageField(upload_to='myimage')
    date=models.DateTimeField(auto_now_add=True)