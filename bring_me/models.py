from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class Todo(models.Model): 
	owner = models.ForeignKey(User) 
	description = models.CharField(max_length=30) 
	done = models.BooleanField() 
	updated = models.DateTimeField(auto_now_add=True)