
from .models import User
from django import forms
from django.forms import ModelForm


class UserRegistrationFrom(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    # Updated Birthday field to use HTML5 date input for modern appearance
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Birthday', required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_password_confirm(self):
        cd = self.cleaned_data
        # Password matching validation
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_confirm']
