import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

import random
from users.models import UserRecord
from faker import Faker

fake = Faker()

def populate(N=5):
  for entry in range(N):
    # create the fake data
    fake_email = fake.email()
    fake_forename = fake.first_name()
    fake_surname = fake.last_name()

    # create the entry
    ur = UserRecord.objects.get_or_create(email=fake_email, forename=fake_forename, surname=fake_surname)[0]

if __name__ == '__main__':
  print('Populating data!')
  populate(50)
  print('Complete')