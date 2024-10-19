from django.shortcuts import render



def dashboard(request):
    # Mock data to simulate contacts
    context = {
        'friends': ['Amy Lee', 'John Doe', 'Jane Smith'],
        'professional': ['Dr. James', 'Lawyer Paul', 'Consultant Lee'],
        'relatives': ['Uncle Bob', 'Aunt Mary'],
        'school': ['Old Classmate Tom', 'Classmate Alex'],
        'love_interests': ['Lover Jess', 'Partner Leo']
    }
    return render(request, 'circle/dashboard.html', context)
