from rest_framework import viewsets
from .models import Volunteer, Event, Task
from .serializers import VolunteerSerializer, EventSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user) # cохраняем объект, связывая его с пользователем, который инициировал запрос


