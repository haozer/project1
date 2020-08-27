from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserRecord

# Create your views here.
def index(request):
  user_list = UserRecord.objects.order_by('forename')
  user_dict = {'user_records':user_list}

  return render(request, 'users/index.html', context=user_dict)
