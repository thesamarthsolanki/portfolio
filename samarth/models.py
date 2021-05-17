from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

# Home Section

class Home(models.Model):
    name = models.CharField(max_length=50)
    greetings1 = models.CharField(max_length=50)
    greetings2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')

    #save time when modified

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# About Section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)


# Skills Section

class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)


# Portfolio Section

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return  f'portfolio {self.id}'

# Contact Form

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name