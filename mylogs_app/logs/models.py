from django.contrib.auth.models import User
from django.db import models

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