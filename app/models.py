from django.db import models
from datetime import datetime

# Create your models here.
class Blog_data(models.Model):
    title=models.CharField(max_length=100)
    details=models.CharField(max_length=10000)
    date=models.DateField()
    
    def __str__(self):
        return self.title