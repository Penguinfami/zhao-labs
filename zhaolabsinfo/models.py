from django.db import models

# Create your models here.
class Teaching(models.Model):
    level = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    courseLink = models.CharField(max_length=300)

class Bio(models.Model):
    positionType = models.CharField(max_length=200)
    positionInfo = models.CharField(max_length=500)

class LabMember(models.Model):
    current = models.BooleanField()
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

class LabPhoto(models.Model):
    url = models.CharField(max_length=200)
    description =  models.CharField(max_length=200, blank=True, null=True)

class Research(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)

class ResearchSubsection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    mainTitle = models.ForeignKey(Research, on_delete=models.CASCADE)

class ContactInfo(models.Model):
    office = models.CharField(max_length=200)
    lab = models.CharField(max_length=200)
    officeTel = models.CharField(max_length=200, blank=True, null=True)
    labTel = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()

class UsefulLink(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=100)

class Publication(models.Model):
    year = models.IntegerField()
    authors = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    pages = models.CharField(max_length=30, blank=True, null=True)
    link = models.CharField(max_length=300, blank=True, null=True)

class Facility(models.Model):
    url = models.CharField(max_length=200)
    description =  models.CharField(max_length=200, blank=True, null=True)

class Opportunity(models.Model):
    content = models.TextField()