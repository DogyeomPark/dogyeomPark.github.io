from django.contrib import admin
from .models import DailySummary, Mood, Medication, Gratitude, UserProfile

admin.site.register(DailySummary)
admin.site.register(Mood)
admin.site.register(Medication)
admin.site.register(Gratitude)
admin.site.register(UserProfile)