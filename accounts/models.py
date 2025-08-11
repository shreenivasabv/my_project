# registration/models.py
from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.username