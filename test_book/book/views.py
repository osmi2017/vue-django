from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import BookSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Book
from django.contrib.sessions.models import Session
from datetime import datetime



# Create your views here.

class BookList(APIView):
    
    def get(self, request, format=None):
            #id=self.request.GET['id']
            #print(id)
            #books= Book.objects.filter(id=id)
            books= Book.objects.all()
            serializer= BookSerializer(books, many=True)
            
            return Response(serializer.data)

    def post(self, request, format=None):
            
        
            serializer = BookSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self,request,  format=None):
           #if request.user.is_authenticated():
            #books= Book.objects.filter(Author=request.user)
            id=self.request.GET['id']
            Book.objects.get(id=id).delete()
            
            
            
            return Response("deleted")

class Useris(APIView):

     def get(self, request, token):
            sessions = Session.objects.filter(expire_date__gte=datetime.now())
            for session in sessions:
                data = session.get_decoded()
                id = data.get('_auth_user_id', None)
                ses = session.session_key
                #print(data)
                if id:
                    name = User.objects.get(id=id)
                    print(data)
            
            return Response(id)
            
                   
        
 

