from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Contact, Profile
from .forms import UserRegistrationFrom
from django.views import generic
from django.contrib.auth import login
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

class ContactDetailView(generic.DetailView):
    model = Contact

def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            Profile.objects.create(user=new_user, birthday=form.cleaned_data.get('birthday'))
            login(request, new_user)
            return redirect('dashboard')
    else:
        form = UserRegistrationFrom()
    return render(request, 'registration/register.html', {'form': form})