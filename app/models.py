from django.db import models


class Volunteer(models.Model):
    user = models.CharField(max_length=200)
    bio = models.TextField()
    joined_date = models.DateField()

    def __str__(self):
        return self.user

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

