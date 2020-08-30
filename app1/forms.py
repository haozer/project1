from django import forms
from app1.models import Topic

class App1Form(forms.ModelForm):
  class Meta:
    model = Topic
    fields = ['top_name']
