from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='projects/')

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)  # e.g., Beginner, Intermediate, Expert

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # blank end date for current jobs

class Acheivments(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Education(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)