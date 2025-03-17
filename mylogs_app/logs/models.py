from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class DailySummary(models.Model):
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Mood(models.Model):
    time_of_day = models.CharField(max_length=20)  # 기상 직후, 오전, 오후, 수면 전
    mood = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Medication(models.Model):
    name = models.CharField(max_length=100)
    taken = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Gratitude(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
