from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Book
        fields=[
            "id",
            "Author",
            "Title",
            "Description",
            "get_image",
            "get_thumbnail",
           


        ]

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User 
        fields=[
            "id",
            "username",
        ]
     