from django.urls import path

from measurement.views import sensor, measurement

urlpatterns = [
    path('measurement/', measurement),
    path('sensor/', sensor)
]

