from django import forms
from django.contrib.auth.models import User
from userprofiles.models import UserProfiles

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ['username', 'email', 'password']

class UserProfilesForm(forms.ModelForm):
  class Meta():
    model = UserProfiles
    fields = ['portfolio_site', 'profile_pic']