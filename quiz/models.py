from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50 ,verbose_name='Category Name' )#verbose_name='Category Name' admin panelde nasıl görünmesini istiyorsak bunu yazarız 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'
        
        
        
class Quiz(models.Model):
    title=models.CharField(max_length=50 ,verbose_name='Quiz  title'  )  
    category=models.ForeignKey(Category,on_delete=models.CASCADE   )      
        
        
        
        
        