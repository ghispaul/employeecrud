from django.db import models

# Create your models here.

class emp(models.Model):
    ename=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    image=models.ImageField(upload_to="image")

    def __str__(self):
        return self.ename


