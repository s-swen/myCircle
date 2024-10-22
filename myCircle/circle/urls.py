from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/<int:pk>', views.ContactDetailView.as_view(), name='contact-detail'),
]
