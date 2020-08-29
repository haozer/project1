from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserRecord
from . import forms

# Create your views here.
def index(request):
  user_list = UserRecord.objects.order_by('forename')
  user_dict = {'user_records':user_list}

  return render(request, 'users/index.html', context=user_dict)

def userForm_view(request):
  theForm = forms.UserForm()

  if request.method == 'POST':
    theForm = forms.UserForm(request.POST)

    if theForm.is_valid():
      # process form
      print("Validation success:")
      print("Forename: " + theForm.cleaned_data['forename'])
      print("Surname: " + theForm.cleaned_data['surname'])
      print("Email: " + theForm.cleaned_data['email'])

      ur = UserRecord.objects.get_or_create(email=theForm.cleaned_data['email'], forename=theForm.cleaned_data['forename'], surname=theForm.cleaned_data['surname'])[0]
      print("User Record created in DB")

  return render(request, 'users/form.html', {'the_form':theForm})
