from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models improt UserProfile

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'logs/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth_date')
        location = request.POST.get('location')

        profile = request.user.profile
        profile.bio = bio
        profile.birth_date = birth_date
        profile.location = location
        profile.save()

        return redirect('profile')
    
    return render(request, 'logs/profile_edit.html',
{'profile': request.user.profile})