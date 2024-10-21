from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def dashboard(request):
    # Get the user's contacts from the database, grouped by category
    user_profile = request.user.profile  # This assumes the Profile is linked to the User model

    contacts = Contact.objects.filter(user=user_profile)

    # Organize contacts into categories
    friends = contacts.filter(category='friend')
    professional = contacts.filter(category='professional')
    relatives = contacts.filter(category='relative')
    school = contacts.filter(category='schoolmate')
    love_interests = contacts.filter(category='love_interest')

    # Pass the contacts into the context
    context = {
        'friends': friends,
        'professional': professional,
        'relatives': relatives,
        'school': school,
        'love_interests': love_interests,
    }
    return render(request, 'circle/dashboard.html', context)
