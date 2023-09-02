from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

def create_superuser(self, email, username, first_name, password, **other_fields):
  other_fields.setdefault('is_staff',True)
  other_fields.setdefault('is_superuser',True)
  other_fields.setdefault('is_active',True)

class CustomAccountManager(BaseUserManager):
  
  def create_user(self,email,username,first_name,password,**other_fields):
    
      if not email :
        raise ValueError(_("You must Provide an email address"))
      email = self.normalize_email(email)
      user = self.model(email=email, username=username,
                        first_name=first_name, **other_fields)
      user.set_password =(password)
      user.save()
      return user


class NewUser(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(_('email address'), unique=True)
  username = models.CharField(max_length=155, unique=True)
  first_name = models.CharField(max_length=155)
  start_date = models.models.DateTimeField(default=timezone.now)
  about = models.TextField(_('about'),max_length=500,blank=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  def __str__(self):
    return self.username