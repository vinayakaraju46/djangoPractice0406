from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    college = models.CharField(max_length=70, blank=False, default='')
    subject = models.CharField(max_length=60, blank=False, default='')