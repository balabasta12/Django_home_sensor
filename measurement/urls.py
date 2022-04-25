from django.urls import path

from measurement.views import SensorsView, SensorViewUpdate, MeasurementView


urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
]


