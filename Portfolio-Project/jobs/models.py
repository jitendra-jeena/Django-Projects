from django.db import models

# Create your models here.
class Job(models.Model):
    # Image
    image = models.ImageField(upload_to="images/")

    #Summary
    summary = models.CharField(max_length=100)

    def __str__(self):
        return self.summary

class Project(models.Model):
    image = models.ImageField(upload_to="images/projects/")
    title = models.CharField(max_length=150)
    tags = models.CharField(max_length=50,default = "all")
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=100,default="#")

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage =   models.IntegerField()
    def __str__(self):
        return self.name

class Certificates(models.Model):
    image = models.ImageField(upload_to="images/certificates/",default="#")
    name = models.CharField(max_length=150)
    tags = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
