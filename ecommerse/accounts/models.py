from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager

# from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class MyAccountManager(BaseUserManager):
  def create_user(self, email, username, first_name, is_staff, is_superuser, password=None, **extra_fields):
    """
    Creates and saves a User with the given email and password.
    """
    now = timezone.now()
    if not email:
      raise ValueError('User must have email address')

    if not username:
      raise ValueError('User must have username')

    email = self.normalize_email(email)
    user = self.model(
      email=email,
      username = username,
      first_name = first_name,
      is_staff=is_staff, is_active=True,
      is_superuser=is_superuser, last_login=now,
      date_joined=now, **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, username, first_name, password, **extra_fields):
    user = self.create_user(
      email = self.normalize_email(email),
      password = password,
      username = username,
      first_name = first_name,
      **extra_fields
    )

    user.is_staff = True
    user.is_admin = True
    user.is_superuser = True

    user.save(using=self._db)
    return user

class Account(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(verbose_name="Email Id", max_length=60, unique=True)
  username = models.CharField(max_length=20, unique=True)
  date_joined = models.DateTimeField(verbose_name="Date join", auto_now_add=True)
  last_login = models.DateTimeField(verbose_name="Last Login", auto_now_add=True)
  is_admin = models.BooleanField(default = False)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [
    'username', 'first_name','is_staff', 'is_superuser', 'password'
  ]

  objects = MyAccountManager()

  def get_full_name(self):
    """
    Returns the first_name plus the last_name, with a space in between.
    The user is identified by their first_name plus last_name
    """
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

  def __str__(self):
    return self.email

  def get_short_name(self):
    "Returns the short name for the user."
    short_name = self.first_name[0].upper()
    return short_name

  def has_perm(self, perm, obj = None):
    '''Does the user have a specific permission?'''
    return self.is_admin

  def has_module_perms(self, app_Label):
    "Does the user have permissions to view the app `app_label`?"
    return True

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()