from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic, Webpage, AccessRecord

# Create your views here.
def home(request):
  #return HttpResponse("Hello Hao!")
  my_dict = {'insert_me':"Goodbye now from view.py!!"}
  return render(request, 'app1/home.html', context=my_dict)

def index(request):
  wp_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records':wp_list}

  return render(request, 'app1/index.html', context=date_dict)

def test(request):
  return HttpResponse("Goodbye!")