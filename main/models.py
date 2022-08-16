from django.db import models

# Create your models here.
from django.db import models

class About(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to="images/")


class Categoriya(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Specialized(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    percentage =models.IntegerField()





class Service(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name

class Portfolio_images(models.Model):
    portfolio = models.ForeignKey(Portfolio, null=True, on_delete=models.CASCADE)
    project_name = models.CharField( max_length=250)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.project_name
