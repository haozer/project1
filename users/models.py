from django.db import models

# Create your models here.
class UserRecord(models.Model):
  email = models.CharField(max_length=264, unique=True)
  forename = models.CharField(max_length=32)
  surname = models.CharField(max_length=32)

  def __str__(self):
    return ' '.join((self.forename, self.surname))
