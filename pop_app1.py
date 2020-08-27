import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

import random
from app1.models import Topic, Webpage, AccessRecord
from faker import Faker

fake = Faker()
topics = ['Search', 'Marketplace', 'News', 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
  return t

def populate(N=5):
  for entry in range(N):
    # get the entry for the topic
    fake_top = add_topic()

    # create the fake data
    fake_url = fake.url()
    fake_date = fake.date()
    fake_name = fake.company()

    # create the entry
    wp = Webpage.objects.get_or_create(topic=fake_top, url=fake_url, name=fake_name)[0]

    # create fake access record
    ar = AccessRecord.objects.get_or_create(name=wp, date=fake_date)[0]

if __name__ == '__main__':
  print('Populating data!')
  populate(20)
  print('Complete')