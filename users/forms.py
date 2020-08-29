from django import forms
from django.core import validators

def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("Value needs to begins with a 'Z'.")

class UserForm(forms.Form):
  forename = forms.CharField(required=True, 
                              validators=[check_for_z])
  surname = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  botcatcher = forms.CharField(required=False, 
                              widget=forms.HiddenInput, 
                              validators=[validators.MaxLengthValidator(0)],
                              )
