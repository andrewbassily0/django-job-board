from random import choices
from tkinter import CASCADE, ON
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import SlugField

# Create your models here.
JOB_TYBE= (
    ("full time","full time"),
    ("part time","part time"),
)



class Job(models.Model):
    title= models.CharField(max_length=100)
    Job_type =models.CharField(max_length=15 ,choices=JOB_TYBE)
    descriptions=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=1)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experiance=models.IntegerField(default=1)
    category = models.ForeignKey('Category', related_name='+',  on_delete=models.CASCADE )
    image = models.ImageField( upload_to='jobs/')

    slug=models.SlugField(blank=True , null=True )

    def save(self, *args , **kwargs):
        self.slug= SlugField(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
      return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Apply(models.Model):
    job=models.ForeignKey('Job' , related_name='apply_job', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    mail=models.EmailField(max_length=100)
    portfoilo=models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=200)
    apply_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

   