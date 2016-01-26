from rest_framework import serializers 
from bring_me.models import Todo 
from django.contrib.auth.models import User 

class UserSerializer(serializers.HyperlinkedModelSerializer): 
	class Meta: 
		model = User 

class RegistrationSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = User 
		fields = ('username', 'password') 

class TodoSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Todo 
		fields = ('id', 'description','done')