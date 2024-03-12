from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """ Manager for user Profiles """
    def create_user(self,email,name,password=None):
        """ Create a new USer Profile """
        if not email:
            raise ValueError('User must provide an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        """ Creat new superuser with the given details in the field """
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

    
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in the system """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects= UserProfileManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    def get_full_name(self):
        """retrive user full name """
        return self.name
    
    def get_short_name(self):
        """ retrive short name of user"""
        return self.name
    
    def __str__(self):
        """retrive string representation of name and other attributes """
        return f'{self.name} {self.email} {self.is_staff} {self.is_active}'