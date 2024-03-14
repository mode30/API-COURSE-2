from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets
# Create your views here.
class HelloApiView(APIView):
    """ Test Api view """
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        """return a list of API view"""
        an_apiview=[
            'Uses Http method as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({
            'message':'Hello','an_apiview':an_apiview
        })
    
    def post(self,request):
        """ create a hello message with our  name"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
    def put(self,request,pk=None):
        """ handle updating an object """
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """handle the deletion of an object"""
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    """ Test api viewsets """
    def list(self,request):
        
        message='hello'
        """ return a hello method"""
        a_viewset=[
            'Uses action(list,create,retrieve,update,destroy)'
            'automatically maps to URLs using Routers'
            'Provides more functionally with code'
        ]
        return Response(
            {
                'message':message,
             'api':a_viewset
             })
    
    def create(self,request,pk=None):
        """ retrieve an objects using the viewset"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name} fan'
            return Response({
                'message':message
            })
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """ update object using viewset"""
        return Response({'http_method':'POST'})
    
    def partial_update(self,request,pk=None):
        """ partially update an object """
        return Response({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        """ destroy or delete an object"""
        return Response({'http_method':'DESTROY'})