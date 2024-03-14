from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
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