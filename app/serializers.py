from rest_framework import serializers
from .models import Volunteer, Event, Task

class VolunteerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = ['id', 'user', 'bio', 'joined_date']

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'name', 'date', 'location', 'organizer']

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

