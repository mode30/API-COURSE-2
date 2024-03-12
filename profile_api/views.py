from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    """ Test Api view """
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
