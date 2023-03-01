from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)
        first_name = first_name

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        COACH = "COACH", 'Coach'
        ATHLETE = "ATHLETE", 'Athlete'

    type = models.CharField(max_length = 8 , choices = Role.choices , 
                            # Default is user is coach
                            default = Role.COACH)


    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True) 
    bio = HTMLField(null=True, blank=True)   
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_athlete = models.BooleanField(default=False)
    is_coach= models.BooleanField(default=False) 

    squads = models.ManyToManyField('Squad', related_name='members', blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.first_name    

    def __str__(self):
        return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
      
    def save(self , *args , **kwargs):
        if not self.type or self.type == None : 
            self.type = User.Role.COACH
        return super().save(*args , **kwargs)

class Squad(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=50, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.location})"
    
class AthleteManager(models.Manager):
    def create_user(self, email, username, password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.user_name(username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def get_queryset(self , *args,  **kwargs):
        coach = kwargs.get('coach', None)
        queryset = super().get_queryset(*args , **kwargs).filter(type=User.Role.ATHLETE)
        if coach is not None:
            queryset = queryset.filter(squads__coach=coach)
        return queryset

class Athlete(User):
    class Meta : 
        proxy = True
    objects = AthleteManager()
      
    def save(self , *args , **kwargs):
        self.type = User.Role.ATHLETE
        self.is_athlete = True
        return super().save(*args , **kwargs)    

class CoachManager(models.Manager):
    def create_user(self , email ,username,firstname, password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email
        )
        user.first_name = (firstname)
        user.user_name(username)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def get_queryset(self , *args , **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = User.Role.COACH)
        return queryset

class Coach(User):
    class Meta :
        proxy = True
        verbose_name_plural = _('coaches')

    objects = CoachManager()
        
      
    def save(self  , *args , **kwargs):
        self.type = User.Role.COACH
        self.is_coach = True
        return super().save(*args , **kwargs)

class SquadMembership(models.Model):
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='memberships')
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coached_squads')
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='squads_joined')
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.athlete.user_name} ({self.squad.name})"

        #############################################################################
        ## the reverse relation for coach can be accessed using coached_squads, #####
        ## and the reverse relation for athlete can be accessed using squads_joined.#
        #############################################################################