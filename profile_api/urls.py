from django.urls import path
from . import views
urlpatterns= [
    
    # path("hello_api",views.HelloApiView.as_view()),
    path("",views.HelloApiView.as_view())
]