
from django.urls import path
from .views import (
    EventListCreateAPIView,
    EventDetailAPIView,
    RegisterForEventAPIView,
    UserRegistrationsAPIView,
)

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('events/<int:event_id>/register/', RegisterForEventAPIView.as_view(), name='event-register'),
    path('registrations/', UserRegistrationsAPIView.as_view(), name='user-registrations'),
]

