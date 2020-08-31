from django.shortcuts import render
from userprofiles.models import UserProfiles
from userprofiles import form

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def register(request):
  user_form = form.UserForm()
  userprofile_form = form.UserProfilesForm()

  if request.method == 'POST':
    user_form = form.UserForm(request.POST)
    userprofile_form = form.UserProfilesForm(request.POST)

    if user_form.is_valid() and userprofile_form.is_valid():
      print("Validation success!")

      # process form
      print("Saving user...")
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = userprofile_form.save(commit=False)
      profile.user = user

      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
      
      profile.save()
      print("User Record created in DB")

      return HttpResponseRedirect(reverse('thank_you'))

    else:
      print(user_form.errors, userprofile_form.errors)

  return render(request, 'userprofiles/form.html', {'user_form':user_form, 'userprofile_form':userprofile_form})

def thank_you(request):
  return render(request, 'userprofiles/thank_you.html')

def index(request):
  user_list = UserProfiles.objects.order_by('portfolio_site')
  user_dict = {'user_records':user_list}

  return render(request, 'userprofiles/index.html', context=user_dict)

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        login(request, user)

        return HttpResponseRedirect(reverse('userprofiles:thank_you'))

      else:
        return HttpResponse('ACCOUNT NOT ACTIVE')

    else:
      print("Someone tried to login and failed!")
      print("Username: {} and Password: {}".format(username, password))

      return HttpResponse("Invalid login details supplied!")
  
  return render(request, 'userprofiles/login.html', {})

@login_required
def user_logout(request):
  logout(request)

  return HttpResponseRedirect(reverse('userprofiles:thank_you'))