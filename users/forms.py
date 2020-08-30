from django import forms
from django.core import validators

def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("Value needs to begins with a 'Z'.")

class UserForm(forms.Form):
  forename = forms.CharField(required=True, label="Forename *", validators=[check_for_z])
  surname = forms.CharField(required=True, label="Surname *")
  email = forms.EmailField(required=True, label="Email *")
  vmail = forms.EmailField(required=True, label="Enter your email again *")
  botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
  #botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

  def clean_botcatcher(self):
    if len(self.cleaned_data['botcatcher']) > 0:
      raise forms.ValidationError("Bot Alert!")
  
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['vmail']

    if email != vmail:
      raise forms.ValidationError("Email Mismatch!")
