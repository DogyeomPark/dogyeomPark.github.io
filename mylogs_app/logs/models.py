from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email Address'), max_length=50, unique=True)
    email_is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Add CustomUserManager
    
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

def get_default_user():
    user = User.objects.first()
    return user.id if user else None

class DailySummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    time_of_day = models.CharField(max_length=20)  # 기상 직후, 오전, 오후, 수면 전
    mood = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=100)
    taken = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Gratitude(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default=get_default_user)
    bio = models.TextField(blank=True ,null=True)