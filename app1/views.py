from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic, Webpage, AccessRecord
from app1.forms import App1Form

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

def form(request):
  theForm = App1Form()

  if request.method == 'POST':
    theForm = App1Form(request.POST)

    if theForm.is_valid():
      # process form
      print("Validation success:")
      print("top_name: " + theForm.cleaned_data['top_name'])

      theForm.save(commit=True)
      print("Topic created in DB, going back to index page...")

      return topics(request)
    else:
      print("Form Error")

  return render(request, 'app1/form.html', {'the_form':theForm})

def topics(request):
  t_list = Topic.objects.order_by('top_name')
  t_dict = {'topics':t_list, 'section':{'title':'Topics', 'parent':'App1'}}

  return render(request, 'app1/topics.html', context=t_dict)