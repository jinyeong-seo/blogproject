from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField('data published')
    writer = models.CharField(max_length=10)
    body = models.TextField()
    
    def __str__(self):
        return self.name
        
    def summary(self):
        return self.body[:100]