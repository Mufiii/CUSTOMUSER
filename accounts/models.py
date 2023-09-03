from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):
      if not email :
          raise ValueError('User Must Have email Address')
      if not password :
          raise ValueError('user Must have the Password')
      user = self.model(
           email = self.normalize_email(email)
      )
      
      user.set_password(password)   
      user.active = is_active
      user.staff = is_staff
      user.admin = is_admin
      user.save(using=self._db)
      return user
    
    def create_staffuser(self,email,password=None):
      user = self.create_user(
          email,
          password=password,
          is_staff = True
      )
      return user
    
    def create_superuser(self,email,password=None):
      user = self.create_user(
          email,
          password=password,
          is_staff = True
      )
      return user
    def create_staffuser(self,email,password=None):
      user = self.create_user(
          email,
          password=password,
          is_staff = True,
          is_admin = True
      )
      return user
    

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    # full_name = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=True) # can Login
    staff = models.BooleanField(default=True) # is staff user
    admin = models.BooleanField(default=True) 
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password is required field by default
    REQUIRED_FIELD = []
    
    def __str__(self):
      return self.email
    
    def get_full_name(self):
      return self.email
    
    def get_short_name(self):
      return self.email
    
    @property
    def is_staff(self):
      return self.staff
    
    @property
    def is_admin(self):
      return self.admin
    
    @property
    def is_active(self):
      return self.active
