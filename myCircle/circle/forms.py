
from .models import User
from django import forms
from django.forms import ModelForm


class UserRegistrationFrom(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    birthday = forms.DateField(widget=forms.SelectDateWidget, label='Birthday', required=False)
    class Meta:
        model = User
        fields = ['username', 'email']
    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_confirm']