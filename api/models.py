from django.db import models

class Info(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    City=models.CharField(max_length=20)
    Admin=models.CharField(max_length=20,default="")
