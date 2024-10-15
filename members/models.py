from django.db import models

# Create your models here.
class Member(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)


class Event(models.Model):
    EventName = models.CharField(max_length=255)
    EventDate = models.DateTimeField()
    EventLocation = models.CharField(max_length=255)
    EventDescription = models.TextField()
    CreatedAt = models.DateTimeField(auto_now_add=True)


