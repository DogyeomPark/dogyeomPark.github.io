from django.db import models

# Create your models here.
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
